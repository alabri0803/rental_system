from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class SystemSettings(models.Model):
  contract_office_fee = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    default=5.000,
    verbose_name=_("رسوم المكتب (ريال عماني)")
  )
  admin_fee = models.DecimalField(
    max_digits=10,
    decimal_places=3,
    default=1.000,
    verbose_name=_("رسوم الإدارة (ريال عماني)")
  )
  commission_rate = models.DecimalField(
    max_digits=5,
    decimal_places=2,
    default=0.03,
    verbose_name=_("نسبة العمولة (%)")
  )
  update_at = models.DateTimeField(
    auto_now=True,
    verbose_name=_("تاريخ التحديث")
  )
  update_by = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    editable=False,
    related_name='updated_settings',
    verbose_name=_("تم التحديث بواسطة")
  )

  class Meta:
    verbose_name = _("إعدادات النظام")
    verbose_name_plural = _("إعدادات النظام")

  def __str__(self):
    return _("إعدادات النظام")