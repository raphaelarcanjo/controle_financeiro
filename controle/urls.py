from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('entrada', views.entrada, name='entrada'),
    path('saida', views.saida, name='saida'),
    path('contato', views.contato, name='contato'),
]
