from rest_framework import serializers
from . models import Jadwal

class ImsyakSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Jadwal 
        fields ='__all__'
