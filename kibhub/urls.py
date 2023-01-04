from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PropertyView,PropertyDetailsView,RegisterView,LoginView,LogoutView, UserView
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('properties/', PropertyView.as_view()),
    path('properties/<int:pk>/', PropertyDetailsView.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
   

]

urlpatterns = format_suffix_patterns(urlpatterns)
