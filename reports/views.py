from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone

from core.models import WorkOrder
from payments.models import RentPayment
from utilities.models import ElectricityBill, WaterBill


# ✅ تقرير الإيجارات
def rent_report_view(request):
    year = request.GET.get('year', timezone.now().year)
    payments = RentPayment.objects.filter(payment_date__year=year)

    total_paid = payments.aggregate(Sum('amount_paid'))['amount_paid__sum'] or 0

    context = {
        'payments': payments.order_by('-payment_date'),
        'total_paid': total_paid,
        'year': year,
    }
    return render(request, 'reports/rent_report.html', context)


# ✅ تقرير المرافق
def utility_report_view(request):
    month = request.GET.get('month', timezone.now().strftime('%Y-%m'))
    water = WaterBill.objects.filter(month=month)
    electricity = ElectricityBill.objects.filter(month=month)

    total_water = sum([w.total_amount for w in water])
    total_electricity = sum([e.total_amount for e in electricity])

    context = {
        'month': month,
        'water_bills': water,
        'electricity_bills': electricity,
        'total_water': total_water,
        'total_electricity': total_electricity,
    }
    return render(request, 'reports/utility_report.html', context)


# ✅ تقرير أوامر العمل
def work_orders_report_view(request):
    orders = WorkOrder.objects.all()
    completed = orders.filter(is_completed=True).count()
    pending = orders.filter(is_completed=False).count()

    context = {
        'orders': orders.order_by('-scheduled_date'),
        'completed': completed,
        'pending': pending,
    }
    return render(request, 'reports/work_orders_report.html', context)
