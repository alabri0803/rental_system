from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
  ROLE_CHOICES = (
    ('admin', _('مشرف')),
    ('staff', _('موظف'))
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
  photo = models.ImageField(
    upload_to='profiles/',
    blank=True,
    null=True,
    verbose_name=_('الصورة الشخصية')
  )

  def __str__(self):
    return self.user.username

  class Meta:
    verbose_name = _('الملف الشخصي')
    verbose_name_plural = _('الملفات الشخصية')