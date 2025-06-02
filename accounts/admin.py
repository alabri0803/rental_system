from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileInline(admin.StackedInline):
  model = UserProfile
  can_delete = False
  verbose_name_plural = 'الملف الشخصي'
  fk_name = 'user'

class CustomUserAdmin(BaseUserAdmin):
  inlines = (UserProfileInline, )
  list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role')

  def get_role(self, obj):
    return obj.profile.get_role_display()
  get_role.short_description = 'الدور'

  def get_inline_instances(self, request, obj=None):
    if not obj:
      return []
    return super().get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'phone', 'role', 'tenant')
  list_filter = ('role',)
  search_fields = ('user__username', 'phone', 'tenant__full_name')