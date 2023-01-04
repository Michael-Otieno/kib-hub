from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.conf import settings
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
      return self.email



class Property(models.Model):
  CATEGORIES = (
    ('house','house'),
    ('office','office'),
    ('shop','shop'),
    ('kibanda','kibanda'),
  )
  description = models.TextField()
  location = models.CharField(max_length=255)
  rooms = models.IntegerField()
  rent = models.IntegerField()
  category = models.CharField(choices=CATEGORIES, default=CATEGORIES[1], max_length=200)
  facilities = models.TextField()
  more_info = models.TextField()
  contacts = models.CharField(blank=True,max_length=200)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True,related_name='properties')
  class Meta:
    ordering = ['id']
  
  def __str__(self):
    return self.description

class PropertyImage(models.Model):
  property_link = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='images')
  image = models.ImageField(upload_to='img',default='img/1.jpg',blank=True) 

