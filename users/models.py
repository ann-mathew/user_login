from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    qualification = models.TextField(max_length=120)

    def __str__(self):
    	return self.name

    def get_absolute_url(self):
    	return reverse("welcome", kwargs={"id": self.id})

    