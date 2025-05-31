from django.urls import path

from .views import ArabicLoginView

urlpatterns = [
  path('login/', ArabicLoginView.as_view(), name='login'),
]