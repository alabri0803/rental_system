from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
import openpyxl
from django.http import HttpResponse
from datetime import date
from .forms import ContractForm
from .models import Contract

def export_contracts_excel(request):
  contracts = Contract.objects.all()
  wb = openpyxl.Workbook()
  ws = wb.active
  ws.title = "العقود"
  headers = [
    "المستأجر",
    "الوحدة",
    "تاريخ البداية",
    "تاريخ النهاية",
    "الإيجار الشهري",
    "رسوم إدارية",
    "مدة العقد",
    "الوقت المتبقي",
    "الحالة",
    "المبلغ الإجمالي",
  ]
  ws.append(headers)
  for contract in contracts:
    remaining = contract.time_remaining
    if contract.is_expired:
      status = "منتهي"
    elif contract.status_color == "orange":
      status = "قريب الانتهاء"
    else:
      status = "ساري"
    ws.append([
      str(contract.tenant),
      str(contract.unit),
      contract.start_date.strftime("%Y-%m-%d"),
      contract.end_date.strftime("%Y-%m-%d"),
      float(contract.monthly_rent),
      float(contract.total_amount),
      contract.contract_duration,
      remaining,
      status,
    ])
  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
  response['Content-Disposition'] = f'attachment; filename=contracts_{date.today()}.xlsx'
  wb.save(response)
  return response
class ContractListView(ListView):
  model = Contract
  template_name = 'contracts/contract_list.html'

class ContractCreateView(CreateView):
  model = Contract
  form_class = ContractForm
  template_name = 'contracts/contract_form.html'
  success_url = reverse_lazy('contract_list')

class ContractUpdateView(UpdateView):
  model = Contract
  form_class = ContractForm
  template_name = 'contracts/contract_form.html'
  success_url = reverse_lazy('contract_list')

class ContractDeleteView(DeleteView):
  model = Contract
  template_name = 'contracts/contract_confirm_delete.html'
  success_url = reverse_lazy('contract_list')