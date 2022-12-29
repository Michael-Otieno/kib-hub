from django.urls import path
from .views import PropertyView

urlpatterns = [
    path('properties/', PropertyView.as_view()),
    # path('land-owner-information/<int:pk>/', LandOwnerDetailInfoView.as_view()),
   

]