from django.contrib import admin

from .models import (
  CommunicationLog,
  Complaint,
  Contact,
  EvictionNotice,
  HelpContact,
  MoveOutNotice,
  ServiceRating,
  UnitReport,
  UnitReportAlbum,
  UnitReportType,
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

@admin.register(UnitReportType)
class UnitReportTypeAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)

class UnitReportAlbumInline(admin.TabularInline):
  model = UnitReportAlbum
  extra = 1
  readonly_fields = ('image',)
  fields = ('image',)

@admin.register(UnitReport)
class UnitReportAdmin(admin.ModelAdmin):
  list_display = ('unit', 'tenant', 'report_type', 'created_at', 'resolved')
  list_filter = ('report_type', 'created_at', 'resolved')
  search_fields = ('unit__unit_number', 'tenant__full_name', 'description')
  inlines = [UnitReportAlbumInline]
  readonly_fields = ('created_at',)

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
  list_display = ('tenant', 'subject', 'created_at', 'resolved')
  list_filter = ('created_at', 'resolved')
  search_fields = ('tenant__full_name', 'subject', 'message')
  readonly_fields = ('created_at',)

@admin.register(HelpContact)
class HelpContactAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'email', 'phone', 'created_at')
  search_fields = ('full_name', 'email', 'phone')
  readonly_fields = ('created_at',)