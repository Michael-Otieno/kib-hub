from .models import Property,PropertyImage,User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  properties = serializers.PrimaryKeyRelatedField(many=True,queryset=Property.objects.all())
  class Meta:
    model = User
    fields = ['id','first_name','last_name','id_number','phone_number','email','properties']

    extra_kwargs = {
      'password':{'write_only':True}
    }

    def create(self,validated_password):
      password = validated_password.pop('password',None)
      instance = self.Meta.model(**validated_password)
      if password is not None:
        instance.set_password(password)
      instance.save()
      return instance


class PropertyImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = PropertyImage
    fields = ['id','property_link','image']



class PropertySerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.email')
  images = PropertyImageSerializer(many=True,read_only=True)
  uploaded_images = serializers.ListField(
    child = serializers.ImageField(max_length=10000,allow_empty_file=False,use_url = False),write_only=True
  )
  class Meta:
    model = Property
    fields = ['id','description','location','rooms','rent','category','facilities','more_info','contacts','images','uploaded_images','owner']

  def create(self, validated_data):
    uploaded_images = validated_data.pop("uploaded_images")
    property_link = Property.objects.create(**validated_data)
    for image in uploaded_images:
      new_property_image = PropertyImage.objects.create(property_link=property_link,image=image)
    return property_link

