from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from tenants.models import Tenant


class UserProfile(models.Model):
  ROLE_CHOICES = (
    ('admin', _('مشرف')),
    ('staff', _('موظف')),
    ('tenant', _('مستأجر')),
  )
  user = models.OneToOneField(
    User, 
    on_delete=models.CASCADE,
    related_name='profile',
    verbose_name=_('المستخدم')
  )
  phone = models.CharField(
    max_length=20,
    blank=True,
    null=True,
    verbose_name=_('رقم الهاتف')
  )
  role = models.CharField(
    max_length=10,
    choices=ROLE_CHOICES,
    default='staff',
    verbose_name=_('الدور')
  )
  tenant = models.OneToOneField(
    Tenant,
    on_delete=models.SET_NULL,
    blank=True,
    null=True,
    related_name='profiles',
    verbose_name=_('المستأجر المرتبط'),
    help_text=_('هذا الحقل مطلوب إذا كان الدور هو مستأجر')
  )

  def __str__(self):
    return f"{self.user.username} ({self.get_role_display()})"

  class Meta:
    verbose_name = _('ملف مستخدم')
    verbose_name_plural = _('ملفات المستخدمين')