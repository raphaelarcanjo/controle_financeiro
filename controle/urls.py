from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('entrada', views.entrada, name='entrada'),
    path('entrada/editar/<id>', views.entrada_editar, name='entrada_editar'),
    path('entrada/excluir/<id>', views.entrada_excluir, name='entrada_excluir'),
    path('saida', views.saida, name='saida'),
    path('saida/editar/<id>', views.saida_editar, name='saida_editar'),
    path('saida/excluir/<id>', views.saida_excluir, name='saida_excluir'),
    path('contato', views.contato, name='contato'),
]
