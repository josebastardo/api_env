#hagamos la vista
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    html=f'<h1> hola </h1> <p> joe </p>'
    #return HttpResponse(html)
    return render(request,"index.html")


