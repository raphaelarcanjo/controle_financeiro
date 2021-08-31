from django.db import models
from datetime import datetime, date


class Entrada(models.Model):
    valor = models.DecimalField(decimal_places=2, max_digits=8)
    data = models.DateField(null=True, default=datetime.now().date())
    fonte = models.CharField(max_length=80)
    extra = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.valor


class Saida(models.Model):
    valor = models.DecimalField(decimal_places=2, max_digits=8)
    data = models.DateField(null=True, default=datetime.now().date())
    fonte = models.CharField(max_length=80)
    superfluo = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.valor