from django.urls import path
from . import views

urlpatterns = [
    path('', views.tabela, name='tabela'),
    path('mes/', views.mess, name='mes'),
]