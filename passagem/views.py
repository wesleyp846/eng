from django.shortcuts import render
from .models import Passagem 

def tabela(request): 
    # Filtra o queryset pelos dias pares do mês 
    passagens = Passagem.objects.filter(data__in=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) 
    # Passa o queryset para o template 
        return render(request, “tabela.html”, {“passagens”: passagens})