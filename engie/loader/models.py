from django.db import models

class Fuel(models.Model):
    gas = models.FloatField(verbose_name="gas(euro/MWh)")
    kerosine = models.FloatField(verbose_name="kerosine(euro/MWh)")
    co2 = models.IntegerField(verbose_name="co2(euro/ton)")
    wind_percentage = models.IntegerField(verbose_name="wind(%)")

class Powerplant(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    efficiency = models.FloatField()
    pmin = models.IntegerField()
    pmax = models.IntegerField()

class Payload(models.Model):
    load = models.IntegerField()
    fuels = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    powerplants = models.ForeignKey(Powerplant, on_delete=models.CASCADE)

class Plant(models.Model):
    name = models.CharField(max_length=100)
    p = models.IntegerField()