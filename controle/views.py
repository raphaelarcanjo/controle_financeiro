from django.http.response import HttpResponse, JsonResponse
from django.db.models import Sum
from django.shortcuts import redirect, render
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
        try:
            if len(request.POST.get('valor')) <= 0:
                raise ValueError('O valor da entrada não pode ser negativo ou zero')
            if len(request.POST.get('fonte')) > 80:
                raise ValueError('A descrição da fonte de entrada está muito grande')
            entrada = models.Entrada()
            entrada.valor = request.POST.get('valor')
            entrada.data = request.POST.get('data')
            entrada.fonte = request.POST.get('fonte')
            entrada.extra = True if request.POST.get('extra') else False
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

def entrada_editar(request, id):
    if request.method == 'POST':
        try:
            if len(request.POST.get('valor')) <= 0:
                raise ValueError('O valor da entrada não pode ser negativo ou zero')
            if len(request.POST.get('fonte')) > 80:
                raise ValueError('A descrição da fonte de entrada está muito grande')
            entrada = models.Entrada.objects.filter(id=id).first()
            entrada.valor = request.POST.get('valor')
            entrada.data = request.POST.get('data')
            entrada.fonte = request.POST.get('fonte')
            entrada.extra = True if request.POST.get('extra') else False
            entrada.save()
            return redirect('entrada')
        except Exception as e:
            print(e)
            form_entrada = request.POST
    form_entrada = models.Entrada.objects.filter(id=id).values().get()
    data = {
        'form_entrada': form_entrada
    }
    return render(request, 'entrada_editar.html', data)

def entrada_excluir(request, id):
    if request.method == 'POST':
        try:
            models.Entrada.objects.filter(id=request.POST.get('id')).delete()
            return redirect('entrada')
        except Exception as e:
            print(e)
    data = {
        'id': id
    }
    return render(request, 'entrada_excluir.html', data)

def saida(request):
    form_saida = {}
    if request.method == 'POST':
        try:
            if len(request.POST.get('valor')) <= 0:
                raise ValueError('O valor da entrada não pode ser negativo ou zero')
            if len(request.POST.get('fonte')) > 80:
                raise ValueError('A descrição da fonte de entrada está muito grande')
            saida = models.Saida()
            saida.valor = request.POST.get('valor')
            saida.data = request.POST.get('data')
            saida.fonte = request.POST.get('fonte')
            saida.extra = True if request.POST.get('extra') else False
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

def saida_editar(request, id):
    if request.method == 'POST':
        try:
            if len(request.POST.get('valor')) <= 0:
                raise ValueError('O valor da saida não pode ser negativo ou zero')
            if len(request.POST.get('fonte')) > 80:
                raise ValueError('A descrição da fonte de saida está muito grande')
            saida = models.Saida.objects.filter(id=id).first()
            saida.valor = request.POST.get('valor')
            saida.data = request.POST.get('data')
            saida.fonte = request.POST.get('fonte')
            saida.superfluo = True if request.POST.get('superfluo') else False
            saida.save()
            return redirect('saida')
        except Exception as e:
            print(e)
            form_saida = request.POST
    form_saida = models.Saida.objects.filter(id=id).values().get()
    data = {
        'form_saida': form_saida
    }
    return render(request, 'saida_editar.html', data)

def saida_excluir(request, id):
    if request.method == 'POST':
        try:
            models.Saida.objects.filter(id=request.POST.get('id')).delete()
            return redirect('saida')
        except Exception as e:
            print(e)
    data = {
        'id': id
    }
    return render(request, 'saida_excluir.html', data)

def contato(request):
    return render(request, 'contato.html')