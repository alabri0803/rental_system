from datetime import date
from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import SystemSettings

OFFICE_FEE = Decimal('5.000')
ADMIN_FEE = Decimal('1.000')
COMMISSION_RATE = Decimal('0.03')

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
    decimal_places=3,
    verbose_name=_("الإيجار الشهري (ريال عماني)")
  )

  def get_system_settings(self):
    try:
      return SystemSettings.objects.first()
    except:
      return None
    
  
  class Meta:
    verbose_name = _("عقد")
    verbose_name_plural = _("العقود")

  def __str__(self):
    return f"عقد {self.tenant.full_name} - {self.unit}"

  @property
  def yearly_rent_total(self):
    return self.monthly_rent * 12

  @property
  def monthly_rent_total(self):
    return self.monthly_rent

  @property
  def registration_fee(self):
    settings = self.get_system_settings()
    if settings:
      commission = self.yearly_rent_total * settings.commission_rate
      return commission + settings.contract_office_fee + settings.admin_fee
    return self.yearly_rent_total * COMMISSION_RATE + OFFICE_FEE + ADMIN_FEE

  @property
  def total_amount(self):
    return self.yearly_rent_total + self.registration_fee

  def format_omr(self, amount):
    return f"{amount:,.3f} ريال عماني"

  @property
  def total_amount_display(self):
    return self.format_omr(self.total_amount)

  @property
  def monthly_rent_display(self):
    return self.format_omr(self.monthly_rent)

  @property
  def yearly_rent_total_display(self):
    return self.format_omr(self.yearly_rent_total)

  @property
  def registration_fee_display(self):
    return self.format_omr(self.registration_fee)

  @property
  def remaining_days(self):
    today = date.today()
    delta = self.end_date - today
    return max(0, delta.days)

  @property
  def remaining_months(self):
    return self.remaining_days // 30

  @property
  def remaining_years(self):
    return self.remaining_days // 365

  @property
  def is_expired(self):
    return date.today() > self.end_date

  @property
  def status_color(self):
    days = self.remaining_days
    if days <= 0:
      return "red"
    elif days <= 30:
      return "orange"
    return "green"

  @property
  def contract_duration(self):
    delta = self.end_date - self.start_date
    years = delta.days // 365
    months = (delta.days % 365) // 30
    days = (delta.days % 365) % 30
    return f"{years} سنة و {months} شهر و {days} يوم"
  
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