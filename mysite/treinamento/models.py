from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Agent(models.Model):
    id = models.AutoField(primary_key=True,)
    name = models.CharField(max_length=200,null=False)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)