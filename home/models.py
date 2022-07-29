from django.db import models
from datetime import date

class Date(models.Model):
    date=models.DateField( auto_now_add=True, primary_key=True)
    sunny = models.IntegerField(default=0)
    rainny = models.IntegerField(default=0)
    snow = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date)
# Create your models here.
