# Generated by Django 5.0.2 on 2025-06-01 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0004_remove_contract_admin_fees_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='المبلغ المدفوع (ريال عماني)')),
                ('date', models.DateField(auto_now_add=True, verbose_name='تاريخ الدفع')),
                ('method', models.CharField(max_length=50, verbose_name='طريقة الدفع')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='contracts.invoice', verbose_name='الفاتورة')),
            ],
            options={
                'verbose_name': 'دفعة',
                'verbose_name_plural': 'المدفوعات',
            },
        ),
    ]
