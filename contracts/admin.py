from django.contrib import admin

from .models import Contract, Invoice

admin.register(Contract)
admin.site.register(Invoice)