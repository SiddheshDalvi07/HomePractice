from rest_framework import serializers
from .models import Drink



# Serializers define the API representation.
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id','name','description']