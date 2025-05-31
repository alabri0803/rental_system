from django.db import models
from django.utils.translation import gettext_lazy as _


class Tenant(models.Model):
  full_name = models.CharField(
    max_length=255,
    verbose_name=_("الاسم الكامل")
  )
  national_id = models.CharField(
    max_length=20,
    unique=True,
    verbose_name=_("رقم الهوية الوطنية")
  )
  phone = models.CharField(
    max_length=20,
    verbose_name=_("رقم الهاتف")
  )
  email = models.EmailField(
    blank=True,
    null=True,
    verbose_name=_("البريد الإلكتروني")
  )
  address = models.TextField(
    verbose_name=_("العنوان")
  )

  class Meta:
    verbose_name = _("مستأجر")
    verbose_name_plural = _("المستأجرين")

  def __str__(self):
    return self.full_name