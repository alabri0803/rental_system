# Generated by Django 5.0.2 on 2025-06-02 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_options_remove_userprofile_photo_and_more'),
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tenant',
            field=models.ForeignKey(blank=True, help_text='هذا الحقل مطلوب إذا كان الدور هو مستأجر', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profiles', to='tenants.tenant', verbose_name='المستأجر المرتبط'),
        ),
    ]
