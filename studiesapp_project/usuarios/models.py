from django.db import models

class Usuario(models.Model):
    email = models.EmailField
    username = models.CharField(max_length=30)
    senha = models.CharField(max_length=100)
    profilePicture = models.ImageField