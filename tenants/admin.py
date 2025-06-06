from django.contrib import admin

from .models import Tenant


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'national_id', 'phone', 'email')
  search_fields = ('full_name', 'national_id', 'phone', 'email')