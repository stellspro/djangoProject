from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, redirect
from .models import Product, ProductCategory
from .forms import AddFormPost
from django.views.generic import ListView, DetailView

# Create your views here.
menu = [{'name': 'Добавить статью', 'url': 'add_post'},
        {'name': 'Обратная связь', 'url': '#'},
        {'name': 'Войти', 'url': '#'}
        ]


class IndexProduct(ListView):
    """Класс представления главной страницы"""
    model = Product
    template_name = 'blogsushi/index.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context


class IndexProduct(ListView):
    """Класс представления главной страницы"""
    model = Product
    template_name = 'blogsushi/index.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        context['category'] = ProductCategory.objects.all()
        return context


class PostDetail(DetailView):
    """Класс представления отдельного поста"""
    model = Product
    template_name = 'blogsushi/postdetail.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        context['category'] = ProductCategory.objects.all()
        return context


# def index(request):
#     name = Product.objects.all()
#     category = ProductCategory.objects.all()
#     context = {
#         'title': 'Главная страница',
#         'product': name,
#         'category': category,
#         'menu': menu
#     }
#     return render(request, 'blogsushi/index.html', context=context)


# def add_post(request):
#     if request.method == 'POST':
#         form = AddFormPost(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddFormPost()
#     context = {
#         'form': form,
#         'title': 'Добавить пост',
#
#     }
#
#     return render(request, 'blogsushi/addpost.html', context=context)


def cats(request, number):
    return HttpResponse(f'a{number}')


def page_not_found(request, exсeption):
    return HttpResponseNotFound('Страница не найдена')
