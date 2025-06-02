from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from buildings.models import Building, Unit
from contracts.models import Contract
from tenants.models import Tenant

from .forms import (
  UnitTourVisitForm,
)
from .models import (
  CommunicationLog,
  Contact,
  EvictionNotice,
  MoveOutNotice,
  ServiceRating,
  UnitTourVisit,
)


@login_required
def dashboard(request):
  today = date.today()
  contracts = Contract.objects.all()

  expiring = contracts.filter(end_date__gt=today, end_date__lte=today + timedelta(days=30))
  expired = contracts.filter(end_date__lt=today)
  active = contracts.filter(end_date__gt=today + timedelta(days=31))
  latest_evictions = EvictionNotice.objects.order_by('-issue_date')[:5]
  latest_moveouts = MoveOutNotice.objects.order_by('-notice_date')[:5]
  recent_contacts = Contact.objects.order_by('-created_at')[:5]
  
  context = {
    'total_buildings': Building.objects.count(),
    'total_units': Unit.objects.count(),
    'total_tenants': Tenant.objects.count(),
    'total_contracts': contracts.count(),
    'active_count': active.count(),
    'expiring_count': expiring.count(),
    'expired_count': expired.count(),
    'latest_evictions': latest_evictions,
    'latest_moveouts': latest_moveouts,
    'recent_contacts': recent_contacts
  }
  return render(request, 'core/dashboard.html', context)

class ContractListView(LoginRequiredMixin, ListView):
  model = Contract
  template_name = 'core/contract_list.html'
  context_object_name = 'contracts'

class UnitTourVisitListView(LoginRequiredMixin, ListView):
  model = UnitTourVisit
  template_name = 'core/unit_tour_list.html'
  context_object_name = 'unit_tour_visits'

class UnitTourVisitCreateView(LoginRequiredMixin, CreateView):
  model = UnitTourVisit
  form_class = UnitTourVisitForm
  template_name = 'core/unit_tour_form.html'
  success_url = reverse_lazy('unit_tour_list')

class MoveOutNoticeListView(LoginRequiredMixin, ListView):
  model = MoveOutNotice
  template_name = 'core/move_out_list.html'
  context_object_name = 'move_out_notices'

class EvictionNoticeListView(LoginRequiredMixin, ListView):
  model = EvictionNotice
  template_name = 'core/eviction_list.html'
  context_object_name = 'eviction_notices'

class ServiceRatingListView(LoginRequiredMixin, ListView):
  model = ServiceRating
  template_name = 'core/service_rating_list.html'
  context_object_name = 'service_ratings'

class CommunicationLogListView(LoginRequiredMixin, ListView):
  model = CommunicationLog
  template_name = 'core/communication_log_list.html'
  context_object_name = 'communication_logs'