from django.urls import path

from .views import dashboard, ContractListView, UnitTourVisitListView, UnitTourVisitCreateView, MoveOutNoticeListView, EvictionNoticeListView, ServiceRatingListView, CommunicationLogListView

urlpatterns = [
  path('', dashboard, name='dashboard'),
  path('contracts/', ContractListView.as_view(), name='contract_list'),
  path('tours/', UnitTourVisitListView.as_view(), name='unit_tour_list'),
  path('tours/add/', UnitTourVisitCreateView.as_view(), name='unit_tour_create'),
  path('moveouts/', MoveOutNoticeListView.as_view(), name='moveouts_list'),
  path('moveouts/add/', MoveOutNoticeListView.as_view(), name='moveouts_add'),
  path('evictions/', EvictionNoticeListView.as_view(), name='evictions_list'),
  path('ratings/', ServiceRatingListView.as_view(), name='ratings_list'),
  path('communications/', CommunicationLogListView.as_view(), name='communications_list')
]