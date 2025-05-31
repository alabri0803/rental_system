from datetime import date
from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _

OFFICE_FEE = 5
ADMIN_FEE = 1

class Contract(models.Model):
  tenant = models.ForeignKey(
    'tenants.Tenant',
    on_delete=models.CASCADE,
    verbose_name=_("المستأجر")
  )
  unit = models.ForeignKey(
    'buildings.Unit',
    on_delete=models.CASCADE,
    verbose_name=_("الوحدة")
  )
  start_date = models.DateField(
    default=date.today,
    verbose_name=_("تاريخ البداية")
  )
  end_date = models.DateField(
    verbose_name=_("تاريخ النهاية")
  )
  monthly_rent = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    verbose_name=_("الإيجار الشهري (ريال عماني)")
  )
  
  class Meta:
    verbose_name = _("عقد")
    verbose_name_plural = _("العقود")

  def __str__(self):
    return f"عقد {self.tenant.full_name} - {self.unit}"

  @property
  def contract_duration(self):
    delta = self.end_date - self.start_date
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    return f"{years} سنة {months} شهر {days} يوم"

  @property
  def time_remaining(self):
    today = date.today()
    if self.end_date < today:
      return "منتهي"
    delta = self.end_date - today
    return f"{delta.days} يوم"

  @property
  def is_expired(self):
    return date.today() > self.end_date

  @property
  def status_color(self):
    today = date.today()
    remaining_days = (self.end_date - today).days
    if remaining_days <= 0:
      return "red"
    elif remaining_days <= 30:
      return "orange"
    return "green"

  @property
  def total_amount(self):
    base = self.monthly_rent * 12
    commission = base * Decimal(0.03)
    return round(base + commission + OFFICE_FEE + ADMIN_FEE, 2)

class Invoice(models.Model):
  contract = models.ForeignKey(
    Contract,
    on_delete=models.CASCADE,
    related_name="invoices",
    verbose_name=_("العقد")
  )
  month = models.PositiveIntegerField(
    verbose_name=_("الشهر")
  )
  year = models.PositiveIntegerField(
    verbose_name=_("السنة")
  )
  issued_date = models.DateField(
    auto_now_add=True,
    verbose_name=_("تاريخ الإصدار")
  )
  is_paid = models.BooleanField(
    default=False,
    verbose_name=_("مدفوع")
  )

  class Meta:
    unique_together = ("contract", "month", "year")
    verbose_name = _("فاتورة")
    verbose_name_plural = _("الفواتير")

  def __str__(self):
    return f"فاتورة {self.contract} - {self.month}/{self.year}"

  @property
  def amount_due(self):
    return self.contract.monthly_rent