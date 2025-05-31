from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ContractForm
from .models import Contract


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