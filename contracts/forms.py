from django import forms

from .models import Contract


class ContractForm(forms.ModelForm):
  class Meta:
    model = Contract
    fields = '__all__'
    widgets = {
      'start_date': forms.DateInput(attrs={'type': 'date'}),
      'end_date': forms.DateInput(attrs={'type': 'date'}),
    }