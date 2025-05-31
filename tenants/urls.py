from django.urls import path

from .views import TenantCreateView, TenantDeleteView, TenantListView, TenantUpdateView

urlpatterns = [
  path('', TenantListView.as_view(), name='tenant_list'),
  path('add/', TenantCreateView.as_view(), name='tenant_add'),
  path('<int:pk>/edit/', TenantUpdateView.as_view(), name='tenant_edit'),
  path('<int:pk>/delete/', TenantDeleteView.as_view(), name='tenant_delete'),
]