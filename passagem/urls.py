from django.urls import path
from . import views

urlpatterns = [
    path('', views.tabela, name='tabela'),
    path('mes/', views.mess, name='mes'),
    path('seleciona_data/', views.seleciona_data, name='seleciona_data'),
]