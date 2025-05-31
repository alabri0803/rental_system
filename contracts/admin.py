from django.contrib import admin

from .models import Contract, Invoice


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
  list_display = ('tenant', 'unit', 'start_date', 'end_date', 'monthly_rent', 'admin_fees', 'total_amount')
  search_fields = ('tenant__full_name', 'unit__unit_number')
  list_filter = ('start_date', 'end_date')
admin.site.register(Invoice)