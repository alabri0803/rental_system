from django import forms

from .models import Payment


class PaymentForm(forms.ModelForm):
  class Meta:
    model = Payment
    fields = ['invoice', 'amount', 'method']
    widgets = {
      'invoice': forms.Select(attrs={'class': 'form-select'}),
      'amount': forms.NumberInput(attrs={'class': 'form-control'}),
      'method': forms.TextInput(attrs={'class': 'form-control'}),
    }