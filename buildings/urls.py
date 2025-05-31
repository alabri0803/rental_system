from django.urls import path

from .views import (
  BuildingCreateView,
  BuildingDeleteView,
  BuildingListView,
  BuildingUpdateView,
  FloorCreateView,
  UnitCreateView,
  export_buildings_excel,
  export_units_excel,
)

urlpatterns = [
  path('', BuildingListView.as_view(), name='building_list'),
  path('add/', BuildingCreateView.as_view(), name='building_add'),
  path('<int:pk>/edit/', BuildingUpdateView.as_view(), name='building_edit'),
  path('<int:pk>/delete/', BuildingDeleteView.as_view(), name='building_delete'),
  
  path('floors/add/', FloorCreateView.as_view(), name='floor_add'),
  path('units/add/', UnitCreateView.as_view(), name='unit_add'),

  path('export/', export_buildings_excel, name='export_buildings_excel'),
  path('units/export/', export_units_excel, name='export_units_excel'),
]