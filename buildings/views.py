import openpyxl
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import BuildingForm, FloorForm, UnitForm
from .models import Building, Floor, Unit


def export_buildings_excel(request):
  wb = openpyxl.Workbook()
  ws = wb.active
  ws.title = "المباني"
  ws.append(["اسم المبني", "العنوان"])
  for building in Building.objects.all():
    ws.append([building.name, building.address])
  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
  response['Content-Disposition'] = 'attachment; filename=buildings.xlsx'
  wb.save(response)
  return response

def export_units_excel(request):
  wb = openpyxl.Workbook()
  ws = wb.active
  ws.title = "الوحدات"
  ws.append(["رقم الوحدة", "الطابق", "المبني", "النوع"])
  for unit in Unit.objects.select_related('floor__building').all():
    ws.append([
      unit.unit_number,
      unit.floor.number,
      unit.floor.building.name,
      "تجارية" if unit.is_commercial else "سكنية",
    ])
  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
  response['Content-Disposition'] = 'attachment; filename=units.xlsx'
  wb.save(response)
  return response
  
class BuildingListView(ListView):
  model = Building
  template_name = 'buildings/building_list.html'


class BuildingCreateView(CreateView):
  model = Building
  form_class = BuildingForm
  template_name = 'buildings/building_form.html'
  success_url = reverse_lazy('building_list')

class BuildingUpdateView(UpdateView):
  model = Building
  form_class = BuildingForm
  template_name = 'buildings/building_form.html'
  success_url = reverse_lazy('building_list')

class BuildingDeleteView(DeleteView):
  model = Building
  template_name = 'buildings/building_confirm_delete.html'
  success_url = reverse_lazy('building_list')

class FloorCreateView(CreateView):
  model = Floor
  form_class = FloorForm
  template_name = 'buildings/floor_form.html'
  success_url = reverse_lazy('building_list')

class UnitCreateView(CreateView):
  model = Unit
  form_class = UnitForm
  template_name = 'buildings/unit_form.html'
  success_url = reverse_lazy('building_list')