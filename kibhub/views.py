from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Property
from .serializers import PropertySerializer

# Create your views here.
class PropertyView(APIView):
  def get(self,request,format=None):
    properties = Property.objects.all()
    serializer = PropertySerializer(properties,many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = PropertySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)