from django.forms import ModelForm
from .models import Birdseed

class BirdseedForm(ModelForm):
  class Meta:
    model = Birdseed
    fields = ['date', 'seed']