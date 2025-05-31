from django.urls import path

from .views import (
  ContractCreateView,
  ContractDeleteView,
  ContractListView,
  ContractUpdateView,
  InvoicePrintView,
  export_contracts_excel,
)

urlpatterns = [
  path('', ContractListView.as_view(), name='contract_list'),
  path('add/', ContractCreateView.as_view(), name='contract_add'),
  path('<int:pk>/edit/', ContractUpdateView.as_view(), name='contract_edit'),
  path('<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete'),
  path('export/', export_contracts_excel, name='export_contracts_excel'),
  path('invoice/<int:pk>/print/', InvoicePrintView.as_view(), name='invoice_print')
]