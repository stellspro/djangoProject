from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse
from.models import Product, ProductCategory


# Create your views here.

def index(request):
    name = Product.objects.get()
    context = {
        'title': 'Главная страница',
        'name': name
    }
    return render(request, 'blogsushi/index.html', context=context)


def cats(request, number):
    return HttpResponse(f'a{number}')


def page_not_found(request, exсeption):
    return HttpResponseNotFound('Страница не найдена')
