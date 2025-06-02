from django.contrib import messages
from django.shortcuts import redirect


def role_required(allowed_roles=[]):
  def decorator(view_func):
    def wrapper(request, *args, **kwargs):
      if not request.user.is_authenticated:
        return redirect('login')
      role = getattr(request.user.profile, 'role', None)
      if role not in allowed_roles:
        return view_func(request, *args, **kwargs)
      messages.error(request, 'ليس لديك الصلاحية للوصول إلى هذه الصفحة.')
      return redirect('dashboard')
    return wrapper
  return decorator