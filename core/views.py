from datetime import date, timedelta

from django.shortcuts import render

from buildings.models import Building, Unit
from contracts.models import Contract
from tenants.models import Tenant


def dashboard(request):
  today = date.today()
  contracts = Contract.objects.all()

  expiring_soon = contracts.filter(end_date__gt=today, end_date__lte=today + timedelta(days=30))
  expired = contracts.filter(end_date__lt=today)
  active = contracts.filter(end_date__gt=today + timedelta(days=31))

  context = {
    'total_buildings': Building.objects.count(),
    'total_units': Unit.objects.count(),
    'total_tenants': Tenant.objects.count(),
    'total_contracts': contracts.count(),
    'expiring_soon': expiring_soon,
    'expired': expired,
    'active_count': active.count(),
    'expiring_count': expiring_soon.count(),
    'expired_count': expired.count(),
  }
  return render(request, 'core/dashboard.html', context)