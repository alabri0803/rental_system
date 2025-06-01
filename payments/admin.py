from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
  list_display = ('invoice', 'amount', 'date', 'method')
  list_filter = ('date', 'method')
  search_fields = ('invoice__contract__tenant__full_name',)