from django.contrib import admin

from .models import Contract, Invoice

admin.site.register(Contract)
admin.site.register(Invoice)