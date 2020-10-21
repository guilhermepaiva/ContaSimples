from django.conf import settings
from django.db import models

# Create your models here.
class Conta(models.Model):
    titular = models.TextField()
    numero = models.TextField()
    saldo = models.FloatField()

class Transacao(models.Model):
    data = models.TextField()
    tipo = models.CharField(max_length=1)
    valor = models.FloatField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default='',

    )
    conta = models.ForeignKey(
        'contas.Conta',
        related_name='transacoes',
        on_delete=models.CASCADE
    )



