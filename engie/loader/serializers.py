from rest_framework import serializers

class FuelSerializer(serializers.Serializer):
    gas = serializers.FloatField(),
    kerosine = serializers.FloatField(),
    co2  = serializers.IntegerField(),
    wind_percentage = serializers.IntegerField(),

class PowerplantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    efficiency = serializers.FloatField()
    pmin = serializers.IntegerField()
    pmax = serializers.IntegerField()

class PayloadSerializer(serializers.Serializer):
    load = serializers.IntegerField() #Can be negative?
    fuels = FuelSerializer(many=False)
    powerplants = PowerplantSerializer(many=True)

class PlantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    p = serializers.IntegerField()

class ResultSerializer(serializers.Serializer):
    powerplants = PlantSerializer(many=True)