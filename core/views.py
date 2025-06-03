from datetime import date, timedelta

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

from buildings.models import Building
from contracts.models import Contract
from tenants.models import Tenant

from .forms import SystemSettingsForm
from .models import SystemSettings


def is_supervisor(user):
  return user.groups.filter(name='مشرف').exists()

@method_decorator(user_passes_test(is_supervisor, login_url='dashboard'), name='dispatch')
class SettingsView(LoginRequiredMixin, TemplateView):
  template_name = 'core/settings.html'
  
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

@method_decorator(user_passes_test(lambda u: u.groups.filter(name='مشرف').exists()), name='dispatch')
class SettingsUpdateView(LoginRequiredMixin, UpdateView):
  model = SystemSettings
  form_class = SystemSettingsForm
  template_name = 'core/settings_form.html'
  success_url = reverse_lazy('settings')