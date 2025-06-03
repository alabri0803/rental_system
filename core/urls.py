from django.urls import path

from .views import (
  SettingsUpdateView,
  dashboard,
)

urlpatterns = [
  path('', dashboard, name='dashboard'),
  path('settings/', SettingsUpdateView.as_view(), name='settings')
]