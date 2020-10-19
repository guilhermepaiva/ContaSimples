from django.db import models

# Create your models here.
class Conta(models.Model):
    titular = models.TextField()
    numero = models.TextField()
    saldo = models.FloatField()
