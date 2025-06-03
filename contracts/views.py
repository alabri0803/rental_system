from datetime import date

import openpyxl
from django import forms
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
  CreateView,
  DeleteView,
  DetailView,
  ListView,
  UpdateView,
)

from buildings.models import Unit

from .forms import ContractForm
from .models import Contract, Invoice


def available_units_api(request):
  building_id = request.GET.get('building_id')
  data = []
  if building_id:
    units = Unit.objects.filter(floor__building_id=building_id)
    for unit in units:
      data.append({
        'id': unit.id,
        'text': f"{unit.unit_number} - {'تجاري' if unit.is_commercial else 'سكني'}"
      })
  return JsonResponse({'results': data})
class ContractListView(LoginRequiredMixin, ListView):
  model = Contract
  template_name = 'contracts/contract_list.html'
  context_object_name = 'contracts'

class ContractCreateView(LoginRequiredMixin, CreateView):
  model = Contract
  form_class = ContractForm
  template_name = 'contracts/contract_form.html'
  success_url = reverse_lazy('contract_list')
  def clean_unit(self):
    unit = self.cleaned_data['unit']
    start = self.cleaned_data['start_date']
    end = self.cleaned_data['end_date']
    if Contract.objects.filter(unit=unit, end_date__gte=date.today()).exists():
      raise forms.ValidationError(_("هذه الوحدة مؤجرة حاليا"))
    return unit

class ContractUpdateView(LoginRequiredMixin, UpdateView):
  model = Contract
  form_class = ContractForm
  template_name = 'contracts/contract_form.html'
  success_url = reverse_lazy('contract_list')

  def test_func(self):
    return self.request.user.groups.filter(name='مشرف').exists()

  def handle_no_permission(self):
    messages.warning(self.request, _("لا تملك صلاحية تنفيذ هذا الإجراءات"))
    return redirect('contract_list')

class ContractDeleteView(LoginRequiredMixin, DeleteView):
  model = Contract
  template_name = 'contracts/contract_confirm_delete.html'
  success_url = reverse_lazy('contract_list')

  def test_func(self):
    return self.request.user.groups.filter(name='مشرف').exists()

  def handle_no_permission(self):
    messages.warning(self.request, _("لا تملك صلاحية تنفيذ هذا الإجراءات"))
    return redirect('contract_list')

class InvoiceDetailView(LoginRequiredMixin, DetailView):
  model = Invoice
  template_name = 'contracts/invoice_print.html'

def export_contracts_excel(request):
  contracts = Contract.objects.all()
  wb = openpyxl.Workbook()
  ws = wb.active
  ws.title = "العقود"
  ws.append(["المستأجر", "الوحدة", "بداية", "نهاية", "المبلغ الشهري", "المدة", "المتبقي", "الحالة"])
  for c in contracts:
    status = "منتهي" if c.is_expired else "قريب الانتهاء" if c.status_color == "orange" else "ساري"
    ws.append([
      str(c.tenant), str(c.unit), c.start_date, c.end_date, float(c.monthly_rent), c.contract_duration, c.time_remaining, status,
    ])
  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
  response['Content-Disposition'] = f'attachment; filename=contracts_{date.today()}.xlsx'
  wb.save(response)
  return response