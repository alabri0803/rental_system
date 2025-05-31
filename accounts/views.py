from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class ArabicLoginView(LoginView):
  template_name = 'login.html'
  success_url = reverse_lazy('dashboard')