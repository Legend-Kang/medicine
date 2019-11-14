from django.db import models

from django.contrib.auth.models import User
# from django.urls import reverse


# Create your models here.
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')

    photo = models.ImageField(upload_to='%d', default='no_image.jpg')

class pillinformation(models.Model):
    name = models.CharField(max_length=100)
    corporation = models.CharField(max_length=100)
    effect = models.CharField(max_length=1000)
    dosage = models.CharField(max_length=100)
    shape = models.CharField(max_length=100)
    char = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    def __str__(self):
        return self.name

