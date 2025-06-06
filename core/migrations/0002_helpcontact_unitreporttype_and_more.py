# Generated by Django 5.0.2 on 2025-06-02 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0002_alter_building_options'),
        ('core', '0001_initial'),
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='الاسم')),
                ('email', models.EmailField(max_length=255, verbose_name='البريد الالكتروني')),
                ('phone', models.CharField(max_length=20, verbose_name='رقم الهاتف')),
                ('message', models.TextField(verbose_name='الرسالة')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='التاريخ')),
            ],
            options={
                'verbose_name': 'اتصال المساعدة',
                'verbose_name_plural': 'اتصالات المساعدة',
            },
        ),
        migrations.CreateModel(
            name='UnitReportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نوع التقرير')),
            ],
            options={
                'verbose_name': 'نوع التقرير',
                'verbose_name_plural': 'أنواع التقارير',
            },
        ),
        migrations.AlterModelOptions(
            name='communicationlog',
            options={'verbose_name': 'سجل التواصل', 'verbose_name_plural': 'سجلات التواصل'},
        ),
        migrations.AlterModelOptions(
            name='evictionnotice',
            options={'verbose_name': 'إشعار الطرد', 'verbose_name_plural': 'إشعارات الطرد'},
        ),
        migrations.AlterModelOptions(
            name='servicerating',
            options={'verbose_name': 'تقييم الخدمة', 'verbose_name_plural': 'تقييمات الخدمة'},
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='الموضوع')),
                ('message', models.TextField(verbose_name='محتوى الشكوى')),
                ('reply', models.TextField(blank=True, null=True, verbose_name='الرد')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('resolved', models.BooleanField(default=False, verbose_name='تم الرد')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant', verbose_name='المستأجر')),
            ],
            options={
                'verbose_name': 'شكوى',
                'verbose_name_plural': 'الشكاوى',
            },
        ),
        migrations.CreateModel(
            name='UnitReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='الوصف')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('resolved', models.BooleanField(default=False, verbose_name='تم الحل')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tenants.tenant', verbose_name='المستأجر')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildings.unit', verbose_name='الوحدة')),
                ('report_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.unitreporttype', verbose_name='نوع التقرير')),
            ],
            options={
                'verbose_name': 'تقرير الوحدة',
                'verbose_name_plural': 'تقارير الوحدات',
            },
        ),
        migrations.CreateModel(
            name='UnitReportAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='unit_reports/', verbose_name='الصورة')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.unitreport', verbose_name='التقرير')),
            ],
            options={
                'verbose_name': 'صورة تقرير الوحدة',
                'verbose_name_plural': 'صور تقارير الوحدات',
            },
        ),
    ]
