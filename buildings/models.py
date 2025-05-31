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

  class Meta:
    verbose_name = _("مبني")
    verbose_name_plural = _("المباني")

  def __str__(self):
    return self.name

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
    return f"وحدة {self.unit_number} ({'محل' if self.is_commercial else 'سكني'})"