from django.urls import path

from .views import (
  BuildingCreateView,
  BuildingDeleteView,
  BuildingDetailView,
  BuildingListView,
  BuildingUpdateView,
  FloorCreateView,
  UnitCreateView,
)

urlpatterns = [
  path('', BuildingListView.as_view(), name='building_list'),
  path('add/', BuildingCreateView.as_view(), name='building_add'),
  path('<int:pk>/', BuildingDetailView.as_view(), name='building_detail'),
  path('<int:pk>/edit/', BuildingUpdateView.as_view(), name='building_edit'),
  path('<int:pk>/delete/', BuildingDeleteView.as_view(), name='building_delete'),
  
  path('floors/add/', FloorCreateView.as_view(), name='floor_add'),
  path('units/add/', UnitCreateView.as_view(), name='unit_add'),
]