from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TenantForm
from .models import Tenant


class TenantListView(LoginRequiredMixin, ListView):
  model = Tenant
  template_name = 'tenants/tenant_list.html'

class TenantCreateView(LoginRequiredMixin, CreateView):
  model = Tenant
  form_class = TenantForm
  template_name = 'tenants/tenant_form.html'
  success_url = reverse_lazy('tenant_list')

class TenantUpdateView(LoginRequiredMixin, UpdateView):
  model = Tenant
  form_class = TenantForm
  template_name = 'tenants/tenant_form.html'
  success_url = reverse_lazy('tenant_list')

class TenantDeleteView(LoginRequiredMixin, DeleteView):
  model = Tenant
  template_name = 'tenants/tenant_confirm_delete.html'
  success_url = reverse_lazy('tenant_list')