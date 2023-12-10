from rest_framework import serializers
from .models import Food
from .models import Crops


class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('studentId','FirstName','LastName','RegistrationNo','Email')

class CropFooderializers(serializers.ModelSerializer):
    class Meta:
        model = Crops
        fields = ('CountryName','item','element','year','unit','value','CropId')



