from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PropertyView,PropertyDetailsView

urlpatterns = [
    path('properties/', PropertyView.as_view()),
    path('properties/<int:pk>/', PropertyDetailsView.as_view()),
   

]

urlpatterns = format_suffix_patterns(urlpatterns)
