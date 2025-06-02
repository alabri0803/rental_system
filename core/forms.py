from django import forms

from .models import (
  CommunicationLog,
  Contact,
  EvictionNotice,
  MoveOutNotice,
  ServiceRating,
  UnitTourVisit,
)


class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = '__all__'

class UnitTourVisitForm(forms.ModelForm):
  class Meta:
    model = UnitTourVisit
    fields = '__all__'

class MoveOutNoticeForm(forms.ModelForm):
  class Meta:
    model = MoveOutNotice
    fields = '__all__'

class EvictionNoticeForm(forms.ModelForm):
  class Meta:
    model = EvictionNotice
    fields = '__all__'

class ServiceRatingForm(forms.ModelForm):
  class Meta:
    model = ServiceRating
    fields = '__all__'

class CommunicationLogForm(forms.ModelForm):
  class Meta:
    model = CommunicationLog
    fields = '__all__'