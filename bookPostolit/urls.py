"""bookPostolit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

from firstapp import views

urlpatterns = [
    # CRUD
    path('', views.crud_index),
    path('create/', views.crud_create),
    path('edit/<int:id>/', views.crud_edit),
    path('delete/<int:id>/', views.crud_delete),

    # TemplateView
    path('about/', TemplateView.as_view(template_name='firstapp/about.html')),
    path('contact/', TemplateView.as_view(template_name='firstapp/contact.html',
                                          extra_context={'work':'development', 'time':60})),

    path('admin/', admin.site.urls),
    path('', views.index),
    path('index_app1', views.index_app1), # http://127.0.0.1:8000/index_app1
    path('contact/', views.contact),  # это правильно. записывать с окончанием на '/'

    # использование регулярных выражений
    re_path(r'^about/contract', views.about),  # более конкретные маршруты располагаются первыми, чем более общие
    re_path(r'^about', views.about), # применяется регулярное выражение: путь должен начинаться со слова about
    re_path(r'^products/(?P<productid>\d+)/', views.products), # маршурт со значением параметра в строке URL
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users), # пример запроса: http://127.0.0.1:8000/users/3/Gary/
    re_path(r'^products/$', views.products), # маршурт по умолчанию, если не будет передано значение параметра в строке URL

    # тоже самое с использованием path:
    path('products/<int:productid>/', views.products),  # пример запроса: http://127.0.0.1:8000/products/4/
    path('users/<int:id>/<name>/', views.users),  # пример запроса: http://127.0.0.1:8000/users/5/Mary/
    path('products/', views.products),  # маршурт при отсутствии параметров в строке URL (по умолчанию)
    path('users/', views.users),  # маршурт по умолчанию

    path('cars/', views.cars),  # http://127.0.0.1:8000/cars/?id=2&name=mers
    path('home/', views.home), # http://127.0.0.1:8000/home/

    path('appindex/', views.appindex),
    path('appabout/', views.appabout), # http://127.0.0.1:8000/appabout/

    path('indexform/', views.indexform),
    path('formfields/', views.formfields),
    path('fieldsdisplay/', views.fieldsdisplay),
    path('valid/', views.valid),

    path('tuningfield/', views.tuningfield),
    path('tuningfield2/', views.tuningfield2),
    path('tuningfield3/', views.tuningfield3),

]
