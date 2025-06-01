from django.contrib import admin

from .models import Contract, Invoice


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
  list_display = ('tenant', 'unit', 'start_date', 'end_date', 'monthly_rent')
  list_filter = ('start_date', 'end_date')
  search_fields = ('tenant__full_name', 'unit__unit_number')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
  list_display = ('contract', 'month', 'year', 'issued_date', 'is_paid')
  list_filter = ('is_paid', 'year', 'month')
  search_fields = ('contract__tenant__full_name',)