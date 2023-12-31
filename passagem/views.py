from django.shortcuts import render, HttpResponse
from .models import Passagem 

def tabela(request): 
    # Filtra o queryset pelos dias pares do mês 
    passagens = Passagem.objects.filter(data__in=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) 
    # Passa o queryset para o template 
    return render(request, "tabelas.html", {"passagens": passagens})

def mess(request):
    from datetime import date

    # Cria um objeto de data com o ano e o mês desejados
    data = date(2023, 4, 1)

    # Gera uma sequência de números de 1 até o último dia do mês
    dias = range(1, data.replace(month=data.month+1, day=1).day)

    # Itera sobre a sequência de números
    for dia in dias:
        # Verifica se o número é par
        if dia % 2 == 0:
            # Formata o número como uma string de data
            data_em_texto = date(data.year, data.month, dia).strftime("%d/%m/%Y")
            # Imprime a string de data
            
            #print(data_em_texto)
    return HttpResponse(data_em_texto, "diasss.html")
