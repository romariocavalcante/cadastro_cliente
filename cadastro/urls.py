from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes_cadastrados', views.clientes_cadastrados, name='clientes_cadastrados'),
]