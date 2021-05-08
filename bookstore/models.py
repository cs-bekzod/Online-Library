from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(AbstractUser):
    is_publisher = models.BooleanField(default=False)
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    pdf = models.FileField(upload_to='bookapp/pdfs/')
    image = models.ImageField(upload_to='bookapp/covers/')

    def __str__(self):
        return self.title

