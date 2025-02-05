from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.listas_produtos_json, name='listar_produtos_json'),
    path('listar-produtos/', views.listar_produtos, name='listar_produtos'),
]
