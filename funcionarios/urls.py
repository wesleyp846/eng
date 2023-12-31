from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar),
    path('', views.home, name='home'),
    path('tabela/', views.tabela, name='tabela'),
]