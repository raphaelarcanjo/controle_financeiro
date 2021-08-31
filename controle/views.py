from django.http.response import HttpResponse, JsonResponse
from django.db.models import Sum
from django.shortcuts import render
from . import models

def home(request):
    entrada = models.Entrada.objects.all().aggregate(Sum('valor'))['valor__sum']
    entrada = 0 if entrada is None else entrada
    saida = models.Saida.objects.all().aggregate(Sum('valor'))['valor__sum']
    saida = 0 if saida is None else saida
    total = entrada - saida
    data = {
        'entrada': entrada,
        'saida': saida,
        'total': total
    }
    return render(request, 'home.html', data)


def entrada(request):
    form_entrada = {}
    if request.method == 'POST':
        entrada = models.Entrada()
        entrada.valor = request.POST.get('valor')
        entrada.data = request.POST.get('data')
        entrada.fonte = request.POST.get('fonte')
        entrada.extra = True if request.POST.get('extra') else False
        try:
            entrada.save()
        except Exception as e:
            print(e)
            form_entrada = request.POST
    entradas = models.Entrada.objects.all()
    total = models.Entrada.objects.all().aggregate(Sum('valor'))['valor__sum']
    data = {
        'form_entrada': form_entrada,
        'entradas': entradas,
        'total': 0 if total is None else total
    }
    return render(request, 'entrada.html', data)


def saida(request):
    form_saida = {}
    if request.method == 'POST':
        saida = models.Saida()
        saida.valor = request.POST.get('valor')
        saida.data = request.POST.get('data')
        saida.fonte = request.POST.get('fonte')
        saida.extra = True if request.POST.get('extra') else False
        try:
            saida.save()
        except Exception as e:
            print(e)
            form_saida = request.POST
    saidas = models.Saida.objects.all()
    total = models.Saida.objects.all().aggregate(Sum('valor'))['valor__sum']
    data = {
        'form_saida': form_saida,
        'saidas': saidas,
        'total': 0 if total is None else total
    }
    return render(request, 'saida.html', data)


def contato(request):
    return render(request, 'contato.html')