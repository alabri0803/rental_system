from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from buildings.models import Building
from contracts.models import Contract
from tenants.models import Tenant


@login_required
def dashboard(request):
  today = date.today()
  contracts = Contract.objects.all()

  active = contracts.filter(end_date__gt=today + timedelta(days=30))
  expiring = contracts.filter(end_date__gt=today, end_date__lte=today + timedelta(days=30))
  expired = contracts.filter(end_date__lt=today)
  
  chart_data = {
    'labels': ['سارية','قريبة الانتهاء','منتهية'],
    'values': [active.count(), expiring.count(), expired.count()],
    'colors': ['#28a745', '#ffc107', '#dc3545'],
  }
  
  context = {
    'total_buildings': Building.objects.count(),
    'total_contracts': contracts.count(),
    'total_tenants': Tenant.objects.count(),
    'chart_data': chart_data,
  }
  return render(request, 'core/dashboard.html', context)