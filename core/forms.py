from django import forms

from .models import SystemSettings


class SystemSettingsForm(forms.ModelForm):
  class Meta:
    model = SystemSettings
    fields = '__all__'
    widgets = {
      'contract_office_fee': forms.NumberInput(attrs={'class':'form-control'}),
      'admin_fee': forms.NumberInput(attrs={'class':'form-control'}),
      'commission_rate': forms.NumberInput(attrs={'class':'form-control'}),
    }