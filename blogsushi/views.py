from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, redirect
from .models import Product, ProductCategory
from .forms import AddFormPost

# Create your views here.
menu = [{'name': 'Добавить статью', 'url': 'add_post'},
        {'name': 'Обратная связь', 'url': '#'},
        {'name': 'Войти', 'url': '#'}
        ]


def index(request):
    name = Product.objects.all()
    category = ProductCategory.objects.all()
    context = {
        'title': 'Главная страница',
        'product': name,
        'category': category,
        'menu': menu
    }
    return render(request, 'blogsushi/index.html', context=context)


def add_post(request):
    if request.method == 'POST':
        form = AddFormPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddFormPost()
    context = {
        'form': form,
        'title': 'Добавить пост',

    }

    return render(request, 'blogsushi/addpost.html', context=context)


def cats(request, number):
    return HttpResponse(f'a{number}')


def page_not_found(request, exсeption):
    return HttpResponseNotFound('Страница не найдена')
