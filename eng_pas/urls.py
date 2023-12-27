from django.contrib import admin
from django.urls import path, include
#from app_funcionarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.home, name='home'),
    path('funcionarios/', include('funcionarios.urls')),
]
