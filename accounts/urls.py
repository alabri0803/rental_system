from django.urls import path

from .views import CustomLoginView, CustomLogoutView, UserCreateView, profile_view

urlpatterns = [
  path('login/', CustomLoginView.as_view(), name='login'),
  path('logout/', CustomLogoutView.as_view(), name='logout'),
  path('profile/', profile_view, name='profile'),
  path('register/', UserCreateView.as_view(), name='user_register'),
]