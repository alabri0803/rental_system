from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المستخدم'}),
      'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم الأول'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم الأخير'})
    }

class UserProfileForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ['phone', 'role', 'tenant']
    widgets = {
      'phone': forms.TextInput(attrs={'class': 'form-control'}),
      'role': forms.Select(attrs={'class': 'form-select'}),
      'tenant': forms.Select(attrs={'class': 'form-select'}),
    }

  def clean(self):
    cleaned_data = super().clean()
    role = cleaned_data.get('role')
    tenant = cleaned_data.get('tenant')

    if role == 'tenant' and not tenant:
      self.add_error("tenant", "يجب ربط المستأجر بحساب إذا كان الدور مستأجر")
    elif role != 'tenant' and tenant:
      cleaned_data['tenant'] = None
    return cleaned_data