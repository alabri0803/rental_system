from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from buildings.models import Unit


# ✅ 1. الفني/العامل
class HiredPersonnel(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=_("الاسم الكامل"))
    specialty = models.CharField(max_length=100, verbose_name=_("التخصص"))
    available = models.BooleanField(default=True, verbose_name=_("متاح للعمل؟"))

    def __str__(self):
        return f"{self.full_name} ({self.specialty})"

    class Meta:
        verbose_name = _("فني/عامل")
        verbose_name_plural = _("الفنيين/العمال")


# ✅ 2. بيانات الاتصال بالفني
class PersonnelContact(models.Model):
    personnel = models.ForeignKey(HiredPersonnel, on_delete=models.CASCADE, related_name="contacts", verbose_name=_("الفني"))
    phone = models.CharField(max_length=20, verbose_name=_("رقم الهاتف"))
    email = models.EmailField(blank=True, null=True, verbose_name=_("البريد الإلكتروني"))

    def __str__(self):
        return f"{self.phone} - {self.personnel}"

    class Meta:
        verbose_name = _("بيانات تواصل الفني")
        verbose_name_plural = _("بيانات التواصل")


# ✅ 3. أمر عمل
class WorkOrder(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name=_("الوحدة"))
    title = models.CharField(max_length=255, verbose_name=_("عنوان الأمر"))
    description = models.TextField(verbose_name=_("وصف المشكلة"))
    personnel = models.ForeignKey(HiredPersonnel, on_delete=models.SET_NULL, null=True, verbose_name=_("الفني المسؤول"))
    scheduled_date = models.DateField(verbose_name=_("تاريخ التنفيذ"))
    is_completed = models.BooleanField(default=False, verbose_name=_("تم التنفيذ؟"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاريخ الإنشاء"))
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_("أضيف بواسطة"))

    def __str__(self):
        return f"{self.title} - {self.unit}"

    class Meta:
        verbose_name = _("أمر عمل")
        verbose_name_plural = _("أوامر العمل")


# ✅ 4. مدفوعات أمر العمل (أجر الفني)
class WorkOrderPayment(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name="payments", verbose_name=_("أمر العمل"))
    amount = models.DecimalField(max_digits=10, decimal_places=3, verbose_name=_("المبلغ"))
    paid_on = models.DateField(auto_now_add=True, verbose_name=_("تاريخ الدفع"))
    notes = models.TextField(blank=True, null=True, verbose_name=_("ملاحظات"))

    def __str__(self):
        return f"💰 {self.amount} - {self.work_order}"

    class Meta:
        verbose_name = _("مدفوعات أمر العمل")
        verbose_name_plural = _("مدفوعات أوامر العمل")
