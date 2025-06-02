from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from .decorators import role_required
from .forms import UserForm, UserProfileForm
from .models import UserProfile


class CustomLoginView(LoginView):
  template_name = 'accounts/login.html'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('dashboard')

class CustomLogoutView(LogoutView):
  next_page = reverse_lazy('login')

@login_required
def profile_view(request):
  user_form = UserForm(instance=request.user)
  profile_form = UserProfileForm(instance=request.user.profile)
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = UserProfileForm(request.POST, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, 'تم تحديث الملف الشخصي بنجاح.')
      return redirect('profile')
  return render(request, 'accounts/profile.html', {
    'user_form': user_form,
    'profile_form': profile_form,
  })

@method_decorator([login_required, role_required(['admin'])], name='dispatch')
class UserCreateView(CreateView):
  model = User
  form_class = UserCreationForm
  template_name = 'accounts/register.html'
  success_url = reverse_lazy('user_register')
  def form_valid(self, form):
    user = form.save()
    UserProfile.objects.create(user=user, role='staff')
    messages.success(self.request, 'تم إنشاء المستخدم بنجاح.')
    return super().form_valid(form)