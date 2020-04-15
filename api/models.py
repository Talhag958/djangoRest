from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)


class Ratings(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ratings = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

 