from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class YelpUser(models.Model):
    user_id = models.CharField(max_length=22, primary_key=True)
    name = models.CharField(max_length=200)
    review_count = models.PositiveIntegerField()
    yelping_since = models.DateField()
    useful = models.PositiveIntegerField()
    funny = models.PositiveBigIntegerField()
    cool = models.PositiveBigIntegerField()
    fans = models.PositiveIntegerField()
    friends = models.ManyToManyField("self")
    elite = ArrayField(
        models.PositiveIntegerField(blank=True),
        size=50,
    )
    average_stars = models.FloatField()
    compliment_hot = models.PositiveIntegerField()
    compliment_more = models.PositiveIntegerField()
    compliment_profile = models.PositiveIntegerField()
    compliment_cute = models.PositiveIntegerField()
    compliment_list = models.PositiveIntegerField()
    compliment_note = models.PositiveIntegerField()
    compliment_plain = models.PositiveIntegerField()
    compliment_cool = models.PositiveIntegerField()
    compliment_funny = models.PositiveIntegerField()
    compliment_writer = models.PositiveIntegerField()
    compliment_photos = models.PositiveIntegerField()

