from django.contrib import admin

from .models import (
  CommunicationLog,
  Contact,
  EvictionNotice,
  MoveOutNotice,
  ServiceRating,
  UnitTourVisit,
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'email', 'created_at')
  search_fields = ('full_name', 'email')

@admin.register(UnitTourVisit)
class UnitTourVisitAdmin(admin.ModelAdmin):
  list_display = ('visitor_name', 'unit', 'visit_date')
  list_filter = ('visitor_name',)
  search_fields = ('visitor_name', 'unit__name_number')

@admin.register(MoveOutNotice)
class MoveOutNoticeAdmin(admin.ModelAdmin):
  list_display = ('tenant', 'contract', 'notice_date', 'move_out_date')
  list_filter = ('notice_date',)
  search_fields = ('tenant__full_name',)

@admin.register(EvictionNotice)
class EvictionNoticeAdmin(admin.ModelAdmin):
  list_display = ('tenant', 'contract', 'issue_date', 'issued_by')
  list_filter = ('issue_date', 'issued_by')

@admin.register(ServiceRating)
class ServiceRatingAdmin(admin.ModelAdmin):
  list_display = ('tenant', 'rating', 'created_at')
  list_filter = ('rating', 'created_at')

@admin.register(CommunicationLog)
class CommunicationLogAdmin(admin.ModelAdmin):
  list_display = ('tenant', 'method', 'subject', 'date_sent')
  list_filter = ('method', 'date_sent')
  search_fields = ('tenant__full_name', 'subject')