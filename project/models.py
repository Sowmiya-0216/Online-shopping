from django.db import models
class Myusers(models.Model):
    mail = models.EmailField()
    phone = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
class Model1(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
