from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, './home.html')

def cadastrar(request):
    return HttpResponse('ola')
    #return render(request, 'cadastrar.html')