from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import generics

from .models import Fuel, Powerplant, Payload, Plant

class FuelSerializer(serializers.ModelSerializer):
    gas = serializers.FloatField(source="gas(euro/MWh)")
    kerosine = serializers.FloatField(source="kerosine(euro/MWh)")
    co2  = serializers.IntegerField(source="co2(euro/ton)")
    wind_percentage = serializers.IntegerField(source="wind(%)")

    class Meta:
        model = Fuel
        fields = ['gas', 'kerosine', 'co2', 'wind_percentage']
        
class PowerplantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    efficiency = serializers.FloatField()
    pmin = serializers.IntegerField()
    pmax = serializers.IntegerField()

class PayloadSerializer(serializers.Serializer):
    load = serializers.IntegerField() #Can it be negative?
    fuels = FuelSerializer(many=False)
    powerplants = PowerplantSerializer(many=True)

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['name', 'p']

class ResultSerializer(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PlantSerializer(queryset, many=True)
        return Response(serializer.data)


