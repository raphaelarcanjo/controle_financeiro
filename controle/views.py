from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

def home(request):
    data = {
        'entrada': 0,
        'saida': 0,
        'caixa': 0
    }
    return render(request, 'home.html', data)


def entrada(request):
    if request.method == 'POST':
        pass
    entrada = request.POST
    data = {
        'entrada': entrada
    }
    return render(request, 'entrada.html', data)


def saida(request):
    if request.method == 'POST':
        pass
    saida = request.POST
    data = {
        'saida': saida
    }
    return render(request, 'saida.html', data)


def contato(request):
    return render(request, 'contato.html')