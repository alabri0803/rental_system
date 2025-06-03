from django import forms
from django_select2.forms import ModelSelect2Widget

from buildings.models import Unit
from tenants.models import Tenant

from .models import Contract


class ContractForm(forms.ModelForm):
  class Meta:
    model = Contract
    fields = ['tenant', 'unit', 'start_date', 'end_date', 'monthly_rent']
    widgets = {
      'tenant': ModelSelect2Widget(
        model=Tenant,
        search_fields=['full_name__icontains'],
      ),
      'unit': ModelSelect2Widget(
        model=Unit,
        search_fields=['unit_number__icontains'],
        dependent_fields={'tenant': 'floor__building'},
      ),
      'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
      'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
      'monthly_rent': forms.NumberInput(attrs={'class': 'form-control'}),
    }