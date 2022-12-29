from django_filters.rest_framework import FilterSet
from .models import Property

class PropertyFilter(FilterSet):
  class Meta:
    model = Property
    fields = {
      'category':['exact'],
      'location':['exact'],
      'rooms':['exact'],
      'rent':['gt','lt']
    }