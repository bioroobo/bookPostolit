from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def products(request, productid=1):
    output = "<h2>Продукт № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id=1, name='Maxi'):
    output = "<h2>Пользователь</h2><h3>id: {0}  Имя:{1}</h3>".format(id, name)
    return HttpResponse(output)


def cars(request):
    id = request.GET.get('id', 0)
    name = request.GET.get('name', 'None')
    output = "<h2>Автомобиль</h2><h3>[id:{0}]</h3><h4>Марка:{1}</h4>".format(id, name)
    return HttpResponse(output)