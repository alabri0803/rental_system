from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import UserForm, UserProfileForm


class CustomLoginView(LoginView):
  template_name = 'accounts/login.html'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('dashboard')

class CustomLogoutView(LogoutView):
  next_page = reverse_lazy('login')

@login_required
def profile_view(request):
  user = request.user
  profile = user.profile

  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=user)
    profile_form = UserProfileForm(request.POST, instance=profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, 'تم تحديث الملف الشخصي بنجاح.')
      return redirect('profile')
  else:
    user_form = UserForm(instance=user)
    profile_form = UserProfileForm(instance=profile)

  return render(request, 'accounts/profile.html', {
    'user_form': user_form,
    'profile_form': profile_form,
  })