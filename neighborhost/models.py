from django.db import models
from django.contrib.auth.models import AbstractUser

class Zipcode(models.Model):
    zipcode_id              = models.CharField(max_length=5, primary_key=True)
    city                    = models.CharField(max_length=27)
    state                   = models.CharField(max_length=35)

class Neighborhood(models.Model):
    neighborhood_id         = models.PositiveIntegerField(primary_key=True)
    neighborhood_name       = models.CharField(max_length=255, default='Not assigned')
    neighborhood_found_when = models.DateTimeField(auto_now_add=True)

class Neighbor(AbstractUser):
    zipcode                 = models.ForeignKey(Zipcode, on_delete=models.CASCADE)
    neighborhood            = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, default=0)
    verified                = models.BooleanField(default=False)
    first_name              = None
    last_name               = None