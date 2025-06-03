from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("اسم المستخدم"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('اسم المستخدم')})
    )
    password = forms.CharField(
        label=_("كلمة المرور"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('كلمة المرور')})
    )