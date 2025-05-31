from django.urls import path

from .views import (
  ContractCreateView,
  ContractDeleteView,
  ContractListView,
  ContractUpdateView,
)

urlpatterns = [
  path('', ContractListView.as_view(), name='contract_list'),
  path('add/', ContractCreateView.as_view(), name='contract_add'),
  path('<int:pk>/edit/', ContractUpdateView.as_view(), name='contract_edit'),
  path('<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete')
]