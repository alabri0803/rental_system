from django.db import models
from django.utils.translation import gettext_lazy as _
from buildings.models import Unit
from tenants.models import Tenant
from contracts.models import Contract
from django.contrib.auth.models import User

class PaymentMethod(models.Model):
  name = models.CharField(
    max_length=255,
    verbose_name=_('طريقة الدفع'),
  )

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = _('طريقة الدفع')
    verbose_name_plural = _('طرق الدفع')

class RentalDetail(models.Model):
  unit = models.ForeignKey(
    Unit,
    on_delete=models.CASCADE,
    verbose_name=_('الوحدة'),
  )
  monthly_rent = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    verbose_name=_('الإيجار الشهري'),
  )
  service_charge = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    verbose_name=_('رسوم الخدمة'),
  )
  is_active = models.BooleanField(
    default=True,
    verbose_name=_('نشط'),
  )

  def __str__(self):
    return f"{self.unit} - {self.monthly_rent}"

  class Meta:
    verbose_name = _('تفاصيل الإيجار')
    verbose_name_plural = _('تفاصيل الإيجار')

class RentPayment(models.Model):
  contract = models.ForeignKey(
    Contract,
    on_delete=models.CASCADE,
    verbose_name=_('العقد'),
  )
  month = models.CharField(
    max_length=20,
    verbose_name=_('الشهر'),
  )
  amount_paid = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    verbose_name=_('المبلغ المدفوع'),
  )
  payment_date = models.DateField(
    verbose_name=_('تاريخ الدفع'),
  )
  method = models.ForeignKey(
    PaymentMethod,
    on_delete=models.SET_NULL,
    null=True,
    verbose_name=_('طريقة الدفع')
  )
  received_by = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    verbose_name=_('استلم بواسطة'),
  )

  def __str__(self):
    return f"{self.contract} - {self.amount}"

  class Meta:
    verbose_name = _('دفع الإيجار')
    verbose_name_plural = _('دفعات الإيجار')

class WaterBill(models.Model):
  unit = models.ForeignKey(
    Unit,
    on_delete=models.CASCADE,
    verbose_name=_('الوحدة'),
  )
  month = models.CharField(
    max_length=20,
    verbose_name=_('الشهر'),
  )
  consumption = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    verbose_name=_('الاستهلاك'),
  )
  rate = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0.800,
    verbose_name=_('السعر'),
  )
  issued_at = models.DateField(
    verbose_name=_('تاريخ الإصدار'),
  )

  def __str__(self):
    return f"{self.unit} - {self.month}"

  @property
  def total_amount(self):
    return self.consumption * self.rate

  class Meta:
    verbose_name = _('فاتورة المياه')
    verbose_name_plural = _('فواتير المياه')

class ElectricityBill(models.Model):
  unit = models.ForeignKey(
    Unit,
    on_delete=models.CASCADE,
    verbose_name=_('الوحدة'),
  )
  month = models.CharField(
    max_length=20,
    verbose_name=_('الشهر'),
  )
  consumption = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    verbose_name=_('الاستهلاك'),
  )
  rate = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0.120,
    verbose_name=_('السعر'),
  )
  issued_at = models.DateField(
    auto_now_add=True,
    verbose_name=_('تاريخ الإصدار')
  )

  def __str__(self):
    return f"{self.unit} - {self.month}"

  @property
  def total_amount(self):
    return self.consumption * self.rate

  class Meta:
    verbose_name = _('فاتورة الكهرباء')
    verbose_name_plural = _('فواتير الكهرباء')

class UtilityPayment(models.Model):
  BILL_TYPES = [
    ('water', _('فاتورة المياه')),
    ('electricity', _('فاتورة الكهرباء')),
  ]
  unit = models.ForeignKey(
    Unit,
    on_delete=models.CASCADE,
    verbose_name=_('الوحدة'),
  )
  bill_type = models.CharField(
    max_length=20,
    choices=BILL_TYPES,
    verbose_name=_('نوع الفاتورة'),
  )
  month = models.CharField(
    max_length=20,
    verbose_name=_('الشهر'),
  )
  amount_paid = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    verbose_name=_('المبلغ المدفوع'),
  )
  payment_date = models.DateField(
    verbose_name=_('تاريخ الدفع'),
  )
  received_by = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    verbose_name=_('استلم بواسطة')
  )

  def __str__(self):
    return f"{self.unit} - {self.bill_type} - {self.month}"

  class Meta:
    verbose_name = _('دفع الفاتورة')
    verbose_name_plural = _('دفعات الفواتير')