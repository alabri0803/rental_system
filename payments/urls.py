from django.urls import path

from .views import PaymentCreateView, PaymentListView

urlpatterns = [
  path('', PaymentListView.as_view(), name='payment_list'),
  path('add/', PaymentCreateView.as_view(), name='payment_add')
]