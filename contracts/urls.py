from django.urls import path

from .views import (
  ContractCreateView,
  ContractDeleteView,
  ContractListView,
  ContractUpdateView,
  InvoiceDetailView,
  available_units_api,
  export_contracts_excel,
)

urlpatterns = [
  path('', ContractListView.as_view(), name='contract_list'),
  path('add/', ContractCreateView.as_view(), name='contract_add'),
  path('<int:pk>/edit/', ContractUpdateView.as_view(), name='contract_edit'),
  path('<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete'),
  path('export/', export_contracts_excel, name='export_contracts_excel'),
  path('invoice/<int:pk>/print/', InvoiceDetailView.as_view(), name='invoice_print'),
  path('available-units/', available_units_api, name='available_units_api'),
]