from django.conf import settings
from django.db import models

# Create your models here.
class KegType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    pints = models.IntegerField()
    canyas = models.IntegerField()
    
    class Meta:
        ordering = ('name',)
