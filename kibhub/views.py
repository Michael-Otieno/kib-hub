from .models import Property
from .serializers import PropertySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .filters import PropertyFilter
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.

class PropertyView(ListCreateAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer
  filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
  filterset_class = PropertyFilter
  search_fields = ['description']
  ordering_fields = ['rent']

class PropertyDetailsView(RetrieveUpdateDestroyAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer
  