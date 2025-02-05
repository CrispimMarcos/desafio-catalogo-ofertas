from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ofertas/', include('ofertas.urls')),
    path('', lambda request: redirect('listar_produtos')),
     path('', TemplateView.as_view(template_name='index.html')),
    
]
