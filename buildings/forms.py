from django import forms

from .models import Building, Floor, Unit


class BuildingForm(forms.ModelForm):
  class Meta:
    model = Building
    fields = '__all__'

class FloorForm(forms.ModelForm):
  class Meta:
    model = Floor
    fields = '__all__'

class UnitForm(forms.ModelForm):
  class Meta:
    model = Unit
    fields = '__all__'