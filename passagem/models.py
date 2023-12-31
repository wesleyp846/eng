from django.db import models


class Passagem(models.Model):
    DATA_CHOICES = [(i, i) for i in range(1, 32)] 
    TRANSPORTE_CHOICES = [
        ("M", "Metrô"), 
        ("O", "Ônibus"), 
        ("I", "Intermunicipal"), 
        ("T", "Trem"), 
        ("B", "Bilhete Único"), 
    ]

    data = models.IntegerField(choices=DATA_CHOICES) 
    transporte = models.CharField(max_length=1, choices=TRANSPORTE_CHOICES) 
    valor = models.DecimalField(max_digits=5, decimal_places=2) 
    origem = models.CharField(max_length=50) 
    destino = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.data}/{self.transporte}/{self.valor}"
