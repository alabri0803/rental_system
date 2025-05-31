from django.shortcuts import render

from contracts.models import Contract


def dashboard(request):
  contracts = Contract.objects.all()
  return render(request, 'dashboard.html', {'contracts': contracts})