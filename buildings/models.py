from django.db import models
from django.utils.translation import gettext_lazy as _


class Building(models.Model):
  name = models.CharField(
    max_length=255,
    verbose_name=_("اسم المبني")
  )
  address = models.TextField(
    verbose_name=_("العنوان")
  )

  def __str__(self):
    return self.name

  @property
  def total_floors(self):
    return self.floors.count()

  @property
  def total_units(self):
    return Unit.objects.filter(floor__building=self).count()

  @property
  def commercial_units(self):
    return Unit.objects.filter(floor__building=self, is_commercial=True).count()

  @property
  def residential_units(self):
    return Unit.objects.filter(floor__building=self, is_commercial=False).count()

  class Meta:
    verbose_name = _("مبني")
    verbose_name_plural = _("المباني")
    ordering = ['name']

class Floor(models.Model):
  building = models.ForeignKey(
    Building,
    on_delete=models.CASCADE,
    related_name='floors',
    verbose_name=_("المبني")
  )
  number = models.PositiveIntegerField(
    verbose_name=_("رقم الطابق")
  )

  class Meta:
    verbose_name = _("طابق")
    verbose_name_plural = _("الطوابق")

  def __str__(self):
    return f"طابق {self.number} - {self.building.name}"

class Unit(models.Model):
  floor = models.ForeignKey(
    Floor,
    on_delete=models.CASCADE,
    related_name='units',
    verbose_name=_("الطابق")
  )
  unit_number = models.CharField(
    max_length=10,
    verbose_name=_("رقم الوحدة")
  )
  is_commercial = models.BooleanField(
    default=False,
    verbose_name=_("هل تجارية؟")
  )

  class Meta:
    verbose_name = _("وحدة")
    verbose_name_plural = _("الوحدات")

  def __str__(self):
    return f"وحدة {self.unit_number} ({'تجاري' if self.is_commercial else 'سكني'})"