from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from buildings.models import Unit
from contracts.models import Contract
from tenants.models import Tenant


class Contact(models.Model):
  full_name = models.CharField(
    max_length=255,
    verbose_name=_('الاسم'),
  )
  email = models.EmailField(
    max_length=255,
    verbose_name=_('البريد الالكتروني'),
  )
  message = models.TextField(
    verbose_name=_('الرسالة'),
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_('التاريخ'),
  )

  def __str__(self):
    return f"{self.full_name} - {self.email}"

  class Meta:
    verbose_name = _('الاتصال')
    verbose_name_plural = _('الاتصالات')

class UnitTourVisit(models.Model):
  visitor_name = models.CharField(
    max_length=255,
    verbose_name=_('اسم الزائر'),
  )
  phone = models.CharField(
    max_length=20,
    verbose_name=_('رقم الهاتف'),
  )
  visit_date = models.DateField(
    verbose_name=_('تاريخ الزيارة'),
  )
  unit = models.ForeignKey(
    Unit,
    on_delete=models.CASCADE,
    verbose_name=_('الوحدة'),
  )
  visit_date = models.DateField(
    verbose_name=_('تاريخ الزيارة'),
  )
  notes = models.TextField(
    verbose_name=_('ملاحظات'),
    blank=True,
    null=True,
  )

  def __str__(self):
    return f"زيارة لـــ {self.unit} - {self.visitor_name}"

  class Meta:
    verbose_name = _('زيارة الوحدة')
    verbose_name_plural = _('زيارات الوحدات')

class MoveOutNotice(models.Model):
  tenant = models.ForeignKey(
    Tenant,
    on_delete=models.CASCADE,
    verbose_name=_('المستأجر'),
  )
  contract = models.ForeignKey(
    Contract,
    on_delete=models.CASCADE,
    verbose_name=_('العقد'),
  )
  notice_date = models.DateField(
    verbose_name=_('تاريخ الإشعار'),
  )
  move_out_date = models.DateField(
    verbose_name=_('تاريخ الإخلاء المتوقع'),
  )
  reason = models.TextField(
    verbose_name=_('سبب الإخلاء'),
  )

  def __str__(self):
    return f" إخلاء لـ {self.tenant}"

  class Meta:
    verbose_name = _('إشعار الإخلاء')
    verbose_name_plural = _('إشعارات الإخلاء')

class EvictionNotice(models.Model):
  tenant = models.ForeignKey(
    Tenant,
    on_delete=models.CASCADE,
    verbose_name=_('المستأجر'),
  )
  contract = models.ForeignKey(
    Contract,
    on_delete=models.CASCADE,
    verbose_name=_('العقد'),
  )
  issue_date = models.DateField(
    verbose_name=_('تاريخ الإصدار'),
  )
  reson = models.TextField(
    verbose_name=_('سبب الطرد'),
  )
  issued_by = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
    verbose_name=_('أصدر بواسطة'),
  )

  def __str__(self):
    return f"طرد لـ {self.tenant}"

  class Meta:
    verbose_name = _('إشعار الطرد')
    verbose_name_plural = _('إشعارات الطرد')

class ServiceRating(models.Model):
  tenant = models.ForeignKey(
    Tenant,
    on_delete=models.CASCADE,
    verbose_name=_('المستأجر'),
  )
  rating = models.IntegerField(
    choices=[(i, str(i)) for i in range(1, 6)],
    verbose_name=_('التقييم'),
  )
  comment = models.TextField(
    blank=True,
    null=True,
    verbose_name=_('التعليق'),
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_('التاريخ'),
  )

  def __str__(self):
    return f"تقييم لـ {self.rating} - {self.tenant}"

  class Meta:
    verbose_name = _('تقييم الخدمة')
    verbose_name_plural = _('تقييمات الخدمة')

class CommunicationLog(models.Model):
  tenant = models.ForeignKey(
    Tenant,
    on_delete=models.CASCADE,
    verbose_name=_('المستأجر'),
  )
  method = models.CharField(
    max_length=50,
    choices=[
      ('call', _('اتصال')),
      ('email', _('بريد إلكتروني')),
      ('whatsapp', _('واتساب')),
      ('sms', _('رسالة نصية')),
    ],
    verbose_name=_('طريقة التواصل'),
  )
  subject = models.CharField(
    max_length=255,
    verbose_name=_('الموضوع'),
  )
  content = models.TextField(
    verbose_name=_('المحتوى'),
  )
  date_sent = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_('تاريخ الإرسال')
  )

  def __str__(self):
    return f"{self.method} - {self.tenant}"

  class Meta:
    verbose_name = _('سجل التواصل')
    verbose_name_plural = _('سجلات التواصل')

class UnitReportType(models.Model):
  name = models.CharField(
    max_length=100,
    verbose_name=_('نوع التقرير'),
  )

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = _('نوع التقرير')
    verbose_name_plural = _('أنواع التقارير')

class UnitReport(models.Model):
  unit = models.ForeignKey(
    Unit,
    on_delete=models.CASCADE,
    verbose_name=_('الوحدة'),
  )
  tenant = models.ForeignKey(
    Tenant,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    verbose_name=_('المستأجر'),
  )
  report_type = models.ForeignKey(
    UnitReportType,
    on_delete=models.SET_NULL,
    null=True,
    verbose_name=_('نوع التقرير'),
  )
  description = models.TextField(
    verbose_name=_('الوصف'),
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_('تاريخ الإنشاء'),
  )
  resolved = models.BooleanField(
    default=False,
    verbose_name=_('تم الحل'),
  )

  def __str__(self):
    return f"{self.report_type} - {self.unit}"

  class Meta:
    verbose_name = _('تقرير الوحدة')
    verbose_name_plural = _('تقارير الوحدات')

class UnitReportAlbum(models.Model):
  report = models.ForeignKey(
    UnitReport,
    on_delete=models.CASCADE,
    related_name='images',
    verbose_name=_('التقرير'),
  )
  image = models.ImageField(
    upload_to='unit_reports/',
    verbose_name=_('الصورة'),
  )

  def __str__(self):
    return f"صورة لـ {self.report.id}"

  class Meta:
    verbose_name = _('صورة تقرير الوحدة')
    verbose_name_plural = _('صور تقارير الوحدات')

class Complaint(models.Model):
  tenant = models.ForeignKey(
    Tenant,
    on_delete=models.CASCADE,
    verbose_name=_('المستأجر'),
  )
  subject = models.CharField(
    max_length=255,
    verbose_name=_('الموضوع'),
  )
  message = models.TextField(
    verbose_name=_('محتوى الشكوى'),
  )
  reply = models.TextField(
    blank=True,
    null=True,
    verbose_name=_('الرد'),
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_('تاريخ الإنشاء'),
  )
  resolved = models.BooleanField(
    default=False,
    verbose_name=_('تم الرد'),
  )

  def __str__(self):
    return f"{self.subject} - {self.tenant}"

  class Meta:
    verbose_name = _('شكوى')
    verbose_name_plural = _('الشكاوى')

class HelpContact(models.Model):
  full_name = models.CharField(
    max_length=255,
    verbose_name=_('الاسم'),
  )
  email = models.EmailField(
    max_length=255,
    verbose_name=_('البريد الالكتروني'),
  )
  phone = models.CharField(
    max_length=20,
    verbose_name=_('رقم الهاتف')
  )
  message = models.TextField(
    verbose_name=_('الرسالة'),
  )
  created_at = models.DateTimeField(
    auto_now_add=True,
    verbose_name=_('التاريخ'),
  )

  def __str__(self):
    return f"{self.full_name}"

  class Meta:
    verbose_name = _('اتصال المساعدة')
    verbose_name_plural = _('اتصالات المساعدة')