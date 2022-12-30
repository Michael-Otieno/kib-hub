from .models import Property,PropertyImage
from rest_framework import serializers



class PropertyImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = PropertyImage
    fields = ['id','property_link','image']



class PropertySerializer(serializers.ModelSerializer):
  images = PropertyImageSerializer(many=True,read_only=True)
  uploaded_images = serializers.ListField(
    child = serializers.ImageField(max_length=10000,allow_empty_file=False,use_url = False),write_only=True
  )
  class Meta:
    model = Property
    fields = ['id','description','location','rooms','rent','category','facilities','more_info','contacts','images','uploaded_images']

  def create(self, validated_data):
    uploaded_images = validated_data.pop("uploaded_images")
    property_link = Property.objects.create(**validated_data)
    for image in uploaded_images:
      new_property_image = PropertyImage.objects.create(property_link=property_link,image=image)
    return property_link

