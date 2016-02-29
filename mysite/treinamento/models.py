from django.db import models

class Agent(models.Model):
    id = models.AutoField(primary_key=True,)
    name = models.CharField(max_length=200,null=False)
    lon = models.FloatField()
    lat = models.FloatField()