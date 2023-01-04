from .models import Property,User
from .serializers import PropertySerializer,UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .filters import PropertyFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = {
        'register':'register/',
        'login':'login/',
        'user':'user/',
        'logout':'logout/',
        'properties':'properties/',
        'properties/<int:pk>/':'properties/<int:pk>/',
    }
    return Response(routes)
class RegisterView(generics.GenericAPIView):
  serializer_class = UserSerializer
  def post(self,request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

class LoginView(generics.GenericAPIView):
  serializer_class = UserSerializer
  def post(self,request):
    email = request.data['email']
    password = request.data['password']

    user = User.objects.get(email=email)
    if user is None:
      raise AuthenticationFailed('User not found')
    if user.check_password(password):
      raise AuthenticationFailed('Incorrect password!')

    payload = {
      'id':user.id,
      'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
      'iat':datetime.datetime.utcnow()
    }
    token = jwt.encode(payload,'secret',algorithm='HS256')
    response = Response()
    response.set_cookie(key='jwt',value=token,httponly=True)
    response.data = {
      'jwt':token
    }
    return response

class UserView(generics.GenericAPIView):
  serializer_class = UserSerializer

  def get(self,request):
    token = request.COOKIES.get('jwt')

    if not token:
      raise AuthenticationFailed('Unauthenticated')
    
    try:
      payload = jwt.decode(token,'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
      raise AuthenticationFailed('Unauthenticated')

    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)

    return Response(serializer.data)
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LogoutView(generics.GenericAPIView):
  serializer_class = UserSerializer
  def post(self,request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
      'message':'success'
    }
    return response

class PropertyView(ListCreateAPIView):
  queryset = Property.objects.all()
  serializer_class = PropertySerializer

  filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
  filterset_class = PropertyFilter
  search_fields = ['description']
  ordering_fields = ['rent']
  pagination_class = PageNumberPagination
  parser_classes = (MultiPartParser, FormParser,FileUploadParser,)
  # parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.)



class PropertyDetailsView(APIView):
  
  def get_object(self, pk):
    try:
      return Property.objects.get(pk=pk)
    except Property.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    prop = self.get_object(pk)
    serializer = PropertySerializer(prop)
    return Response(serializer.data)

  permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
  def put(self, request, pk, format=None):
    prop = self.get_object(pk)
    serializer = PropertySerializer(prop, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    prop = self.get_object(pk)
    prop.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  