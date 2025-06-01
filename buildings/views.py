from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q, Max
from django.urls import reverse_lazy
from django.views.generic import (
  CreateView,
  DeleteView,
  DetailView,
  ListView,
  UpdateView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BuildingForm, FloorForm, UnitForm
from .models import Building, Floor, Unit


class BuildingListView(LoginRequiredMixin, ListView):
  model = Building
  template_name = 'buildings/building_list.html'
  context_object_name = 'buildings'
  paginate_by = 10

  def get_queryset(self):
    queryset = Building.objects.annotate(
      total_floor=Count('floors'),
      total_unit=Count('floors__units'),
      commercial_unit=Count('floors__units', filter=Q(floors__units__is_commercial=True)),
      residential_unit=Count('floors__units', filter=Q(floors__units__is_commercial=False)),
    )
    q = self.request.GET.get('q')
    if q:
      queryset = queryset.filter(
        Q(name__icontains=q) | Q(address__icontains=q)
      )
    return queryset

  

class BuildingDetailView(LoginRequiredMixin, DetailView):
  model = Building
  template_name = 'buildings/building_detail.html'
  context_object_name = 'building'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['floors'] = self.object.floors.prefetch_related('units').order_by('number')
    return context

class BuildingCreateView(LoginRequiredMixin, CreateView):
  model = Building
  form_class = BuildingForm
  template_name = 'buildings/building_form.html'
  success_url = reverse_lazy('building_list')
  success_message = 'إضافة المبني بنجاح'

class BuildingUpdateView(LoginRequiredMixin, UpdateView):
  model = Building
  form_class = BuildingForm
  template_name = 'buildings/building_form.html'
  success_url = reverse_lazy('building_list')
  success_message = 'تم تحديث بيانات المبني'

class BuildingDeleteView(LoginRequiredMixin, DeleteView):
  model = Building
  template_name = 'buildings/building_confirm_delete.html'
  success_url = reverse_lazy('building_list')
  success_message = 'تم حذف المبني بنجاح'

class FloorCreateView(LoginRequiredMixin, CreateView):
  model = Floor
  form_class = FloorForm
  template_name = 'buildings/floor_form.html'
  success_url = reverse_lazy('building_list')
  success_message = 'تمت إضافة الطابق بنجاح'

  def get_initial(self):
    initial = super().get_initial()
    building_id = self.request.GET.get('building')
    if building_id:
      building = get_object_or_404(Building, pk=building_id)
      initial['building'] = building
      last_number = Floor.objects.filter(building=building).aggregate(Max('number'))['number__max'] or 0
      initial['number'] = last_number + 1
    return initial

  def form_valid(self, form):
    building = form.cleaned_data['building']
    number = form.cleaned_data['number']
    if Floor.objects.filter(building=building, number=number).exists():
      form.add_error('number', f"الطابق رقم {number} موجود بالفعل في المبني")
      return self.form_invalid(form)
    return super().form_valid(form)

class UnitCreateView(LoginRequiredMixin, CreateView):
  model = Unit
  form_class = UnitForm
  template_name = 'buildings/unit_form.html'
  success_url = reverse_lazy('building_list')
  success_message = 'تمت إضافة الوحدة بنجاح'
  