from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import UserProfile

User = get_user_model()
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'phone', 'role', 'tenant')
  list_filter = ('role',)
  search_fields = ('user__username', 'user__email', 'phone')