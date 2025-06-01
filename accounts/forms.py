from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ['phone', 'role', 'photo']
    widgets = {
      'phone': forms.TextInput(attrs={'class': 'form-control'}),
      'role': forms.Select(attrs={'class': 'form-select'}),
      'photo': forms.FileInput(attrs={'class': 'form-control'}),
    }

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email']
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
    }