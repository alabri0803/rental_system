from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import PaymentForm
from .models import Payment


class PaymentListView(LoginRequiredMixin, ListView):
  model = Payment
  template_name = 'payments/payment_list.html'

class PaymentCreateView(LoginRequiredMixin, CreateView):
  model = Payment
  form_class = PaymentForm
  template_name = 'payments/payment_form.html'
  success_url = reverse_lazy('payment_list')