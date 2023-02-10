from rest_framework import serializers
from .models import MenuTable, BookingTable



#Create the Serializer Fields
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTable
        fields = '__all__'

class BookingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'

        
        




