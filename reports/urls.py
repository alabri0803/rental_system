from django.urls import path

from .views import rent_report_view, utility_report_view, work_orders_report_view

urlpatterns = [
    path('rent/', rent_report_view, name='rent_report'),
    path('utility/', utility_report_view, name='utility_report'),
    path('work-orders/', work_orders_report_view, name='work_orders_report'),
]
