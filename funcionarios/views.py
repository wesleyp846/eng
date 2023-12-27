from django.shortcuts import render
from django.http import HttpResponse

def cadastrar(request):
    return HttpResponse('ola')

def home(request):
    return render(request, './home.html')