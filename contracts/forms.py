from django import forms

from .models import Contract, Invoice


class ContractForm(forms.ModelForm):
  class Meta:
    model = Contract
    fields = ['tenant', 'unit', 'start_date', 'end_date', 'monthly_rent']
    widgets = {
      'tenant': forms.Select(attrs={'class': 'form-select'}),
      'unit': forms.Select(attrs={'class': 'form-select'}),
      'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
      'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
      'monthly_rent': forms.NumberInput(attrs={'class': 'form-control'}),
    }

class InvoiceForm(forms.ModelForm):
  class Meta:
    model = Invoice
    fields = ['contract', 'month', 'year', 'is_paid']
    widgets = {
      'contract': forms.Select(attrs={'class': 'form-select'}),
      'month': forms.NumberInput(attrs={'class': 'form-control'}),
      'year': forms.NumberInput(attrs={'class': 'form-control'}),
      'is_paid': forms.CheckboxInput(attrs={'class': 'form-check-input'})
    }