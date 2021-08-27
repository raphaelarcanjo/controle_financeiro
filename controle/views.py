from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

def Home(request):
    data = {}
    return render(request, 'home.html', data)