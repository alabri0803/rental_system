from django import forms

from .models import Tenant


class TenantForm(forms.ModelForm):
  class Meta:
    model = Tenant
    fields = '__all__'
    widgets = {
      'full_name': forms.TextInput(attrs={'class': 'form-control'}),
      'national_id': forms.TextInput(attrs={'class': 'form-control'}),
      'phone': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
    }