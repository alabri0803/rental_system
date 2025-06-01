from django.contrib import admin

from .models import Building, Floor, Unit


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
  list_display = ('name', 'address')
  search_fields = ('name', 'address')

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
  list_display = ('number', 'building')
  list_filter = ('building',)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
  list_display = ('unit_number', 'floor', 'is_commercial')
  list_filter = ('floor__building', 'is_commercial')
  search_fields = ('unit_number',)