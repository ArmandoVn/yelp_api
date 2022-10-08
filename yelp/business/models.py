from contextlib import nullcontext
from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.
class Business(models.Model):
    business_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
    stars = models.FloatField()
    review_count = models.PositiveIntegerField(default=0)
    is_open = models.PositiveIntegerField(default=0)
    attributes = models.JSONField(null=True)
    categories = models.TextField(null=True, blank=True)
    hours = models.JSONField(null=True)
