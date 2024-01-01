from django.shortcuts import render, HttpResponse, redirect
from .models import Passagem 

def tabela(request):
    # Passa o queryset para o template 
    return render(request, "tabelas.html")

def mess(request):
    from datetime import date, timedelta
    ano=2024
    mes=2
    #mes = request.session.get('mes')
    #ano = request.session.get('ano')
    primeiro_dia = date(ano, mes, 1)
                   
    # Calcula o primeiro dia do próximo mês
    primeiro_dia_proximo_mes = date(ano + (mes // 12), (mes % 12) + 1, 1)

    # Calcula o último dia do mês atual
    ultimo_dia_mes_atual = primeiro_dia_proximo_mes - timedelta(days=1)

    # Gera uma sequência de números de 1 até o último dia do mês
    dias = list(range(1, ultimo_dia_mes_atual.day + 1))
    
    dias_pares = []
    dias_impares = []

    for dia in dias:
    # Verifica se o número é par
        if dia % 2 == 0:
            dias_pares.append(dia)
        else:
            dias_impares.append(dia)

    return render(request, 'diasss.html', {'primeiro': primeiro_dia, 'proximo': primeiro_dia_proximo_mes, 'ultimo_dia': ultimo_dia_mes_atual, 'lista': dias, 'dias_pares': dias_pares, 'dias_impares': dias_impares})

def seleciona_data(request):
    
    return render(request, 'form_mes.html')

def pega_mes(request):
    mes = request.POST.get('mes')
    ano = request.POST.get('ano')

        # Armazena os valores na sessão
    request.session['mes'] = mes
    request.session['ano'] = ano