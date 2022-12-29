from django.db import models

# Create your models here.

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

  class Meta:
    ordering = ['id']