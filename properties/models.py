from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class County(models.Model):
  name = models.CharField(
    max_length=255,
    verbose_name=_('المحافظة'),
  )

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = _('المحافظة')
    verbose_name_plural = _('المحافظات')

class Estate(models.Model):
  name = models.CharField(
    max_length=200,
    verbose_name=_('المجمع'),
  )
  county = models.ForeignKey(
    County,
    on_delete=models.CASCADE,
    verbose_name=_('المحافظة'),
  )
  description = models.TextField(
    verbose_name=_('الوصف'),
  )

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = _('المجمع')
    verbose_name_plural = _('المجمعات')

class EstateBuilding(models.Model):
  estate = models.ForeignKey(
    Estate,
    on_delete=models.CASCADE,
    verbose_name=_('المجمع'),
  )
  name = models.CharField(
    max_length=255,
    verbose_name=_('اسم المبنى'),
  )
  address = models.CharField(
    max_length=255,
    verbose_name=_('العنوان'),
  )

  def __str__(self):
    return f"{self.name} - {self.estate}"

  class Meta:
    verbose_name = _('مبنى المجمع')
    verbose_name_plural = _('مباني المجمع')

class UnitType(models.Model):
  name = models.CharField(
    max_length=255,
    verbose_name=_('نوع الوحدة'),
  )

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = _('نوع الوحدة')
    verbose_name_plural = _('أنواع الوحدات')

class RentalUnit(models.Model):
  building = models.ForeignKey(
    EstateBuilding,
    on_delete=models.CASCADE,
    verbose_name=_('المبنى'),
  )
  unit_type = models.ForeignKey(
    UnitType,
    on_delete=models.CASCADE,
    verbose_name=_('نوع الوحدة'),
  )
  unit_number = models.CharField(
    max_length=255,
    verbose_name=_('رقم الوحدة'),
  )
  floor = models.PositiveIntegerField(
    verbose_name=_('الطابق'),
  )
  size = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    verbose_name=_('المساحة'),
  )
  is_available = models.BooleanField(
    default=True,
    verbose_name=_('متاح'),
  )

  def __str__(self):
    return f"{self.unit_number} - {self.building}"

  class Meta:
    verbose_name = _('وحدة للإيجار')
    verbose_name_plural = _('وحدات للإيجار')
    unique_together = ('building', 'unit_number')

class UnitImage(models.Model):
  unit = models.ForeignKey(
    RentalUnit,
    on_delete=models.CASCADE,
    related_name='images',
    verbose_name=_('الوحدة'),
  )
  image = models.ImageField(
    upload_to='unit_images/',
    verbose_name=_('الصورة'),
  )
  caption = models.CharField(
    max_length=255,
    blank=True,
    null=True,
    verbose_name=_('التعليق'),
  )

  def __str__(self):
    return f"صورة لـ {self.unit.unit_number}"

  class Meta:
    verbose_name = _('صورة الوحدة')
    verbose_name_plural = _('صور الوحدات')

class MaintenanceRequest(models.Model):
  unit = models.ForeignKey(
    RentalUnit,
    on_delete=models.CASCADE,
    verbose_name=_('الوحدة'),
  )
  subject = models.CharField(
    max_length=255,
    verbose_name=_('الموضوع'),
  )
  description = models.TextField(
    verbose_name=_('الوصف'),
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_('تاريخ الإنشاء'),
  )
  scheduled_date = models.DateField(
    blank=True,
    null=True,
    verbose_name=_('تاريخ الجدولة'),
  )
  created_by = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    verbose_name=_('أنشئ بواسطة'),
  )

  def __str__(self):
    return f"{self.subject} - {self.unit.unit_number}"

  class Meta:
    verbose_name = _('طلب الصيانة')
    verbose_name_plural = _('طلبات الصيانة')