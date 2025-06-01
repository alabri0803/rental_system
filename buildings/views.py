from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import BuildingForm, FloorForm, UnitForm
from .models import Building, Floor, Unit


class BuildingListView(LoginRequiredMixin, ListView):
  model = Building
  template_name = 'buildings/building_list.html'
  context_object_name = 'buildings'

class BuildingCreateView(LoginRequiredMixin, CreateView):
  model = Building
  form_class = BuildingForm
  template_name = 'buildings/building_form.html'
  success_url = reverse_lazy('building_list')

class BuildingUpdateView(LoginRequiredMixin, UpdateView):
  model = Building
  form_class = BuildingForm
  template_name = 'buildings/building_form.html'
  success_url = reverse_lazy('building_list')

class BuildingDeleteView(LoginRequiredMixin, DeleteView):
  model = Building
  template_name = 'buildings/building_confirm_delete.html'
  success_url = reverse_lazy('building_list')

class FloorCreateView(LoginRequiredMixin, CreateView):
  model = Floor
  form_class = FloorForm
  template_name = 'buildings/floor_form.html'
  success_url = reverse_lazy('building_list')

class UnitCreateView(LoginRequiredMixin, CreateView):
  model = Unit
  form_class = UnitForm
  template_name = 'buildings/unit_form.html'
  success_url = reverse_lazy('building_list')
  