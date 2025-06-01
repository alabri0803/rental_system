from django.db import models
from django.utils.translation import gettext_lazy as _

from contracts.models import Invoice


class Payment(models.Model):
  invoice = models.ForeignKey(
    Invoice,
    on_delete=models.CASCADE,
    related_name="payments",
    verbose_name=_("الفاتورة")
  )
  amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    verbose_name=_("المبلغ المدفوع (ريال عماني)")
  )
  date = models.DateField(
    auto_now_add=True,
    verbose_name=_("تاريخ الدفع")
  )
  method = models.CharField(
    max_length=50,
    verbose_name=_("طريقة الدفع")
  )

  def __str__(self):
    return f"دفع {self.amount} ريال عماني - {self.date}"

  class Meta:
    verbose_name = _("دفعة")
    verbose_name_plural = _("المدفوعات")