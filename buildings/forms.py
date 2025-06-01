from django import forms

from .models import Building, Floor, Unit


class BuildingForm(forms.ModelForm):
  class Meta:
    model = Building
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
    }

class FloorForm(forms.ModelForm):
  class Meta:
    model = Floor
    fields = '__all__'
    widgets = {
      'building': forms.Select(attrs={'class': 'form-select'}),
      'number': forms.NumberInput(attrs={'class': 'form-control'}),
    }

class UnitForm(forms.ModelForm):
  class Meta:
    model = Unit
    fields = '__all__'
    widgets = {
      'floor': forms.Select(attrs={'class': 'form-select'}),
      'unit_number': forms.TextInput(attrs={'class': 'form-control'}),
      'is_commercial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }