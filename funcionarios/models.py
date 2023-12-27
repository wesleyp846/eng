from django.db import models
from datetime import date

class Colaboradores(models.Model):
    nome = models.CharField(max_length=50)
    TIPO_CHOICES = [
        ('par', 'Par'),
        ('impar', 'Ímpar'),
        ('diarista', 'Diarista'),
    ]
    tipo_colaborador = models.CharField(
        max_length=8,
        choices=TIPO_CHOICES,
        default='diarista',  # escolha padrão
    )
    metro = models.BooleanField(default=False)   
    onibus = models.BooleanField(default=False)   
    intermunicipal = models.BooleanField(default=False)   
    trem = models.BooleanField(default=False)   
    bilhete_unico = models.BooleanField(default=False)
    data_cadastro = models.DateField(default=date.today)
    class Meta:
        verbose_name = 'Colaboradore'

    def __str__(self):
        return self.nome