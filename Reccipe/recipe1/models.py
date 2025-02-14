from django.db import models
from django.contrib.auth.models import User # this User is bulit in

# Create your models here.
class Recepie(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")



