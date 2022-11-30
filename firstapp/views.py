from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

from firstapp.forms import UserForm


def index(request):
    #resp =  HttpResponse("<h2>Главная</h2>")
    resp = render(request, "index.html")
    return resp


def index_app1(request):
    categories = ["Printers", "Scaners", "Monitors", "Discs"]
    addr = ('5-avenu', 26, 40)
    user = {'name':'Pieter',
            'age':20 }
    data = {'header':'transport parameters to template',
            'message':'downloaded template',
            'addr':addr,
            'user':user,
            'categories':categories }
    resp = render(request, "firstapp/index_app1.html", context=data)
    resp = TemplateResponse(request, "firstapp/index_app1.html", data)
    return resp

def appindex(request):
    resp = render(request, "firstapp/appindex.html")
    return resp

def appabout(request):
    resp = render(request, "firstapp/appabout.html")
    return resp

def home(request):
    resp = render(request, "firstapp/home.html")
    resp = TemplateResponse(request, "firstapp/home.html")
    return resp

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


def indexform(request):
    if request.method == "POST":
        name = request.POST.get('name') # получить значение поля name
        age = request.POST.get('age')
        output = '<h2>User</h2><h3>Name - {0}, Age - {1}</h3>'.format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        resp = render(request, "firstapp/indexform.html", {'form':userform})
        return resp

