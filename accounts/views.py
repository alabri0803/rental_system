from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
  template_name = 'accounts/login.html'
  redirect_authenticated_user = True
  success_url = reverse_lazy('dashboard')

class CustomLogoutView(LogoutView):
  next_page = reverse_lazy('login')