from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from .utils import DataMixin
from .models import Product, ProductCategory
from .forms import AddFormPost, FormUser
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
class IndexProduct(DataMixin, ListView):
    """Класс представления главной страницы"""
    model = Product
    template_name = 'blogsushi/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(con.items()))

    def get_queryset(self):
        return Product.objects.filter(is_published=True).select_related('category')


class PostDetail(DataMixin, DetailView):
    """Класс представления отдельного поста"""
    model = Product
    template_name = 'blogsushi/postdetail.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title=context['post'])
        return context


class ShowCategories(DataMixin, ListView):
    """Отображение категорий продуктов"""
    model = Product
    template_name = 'blogsushi/index.html'
    context_object_name = 'posts'
    allow_empty = True

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowCategories, self).get_context_data(**kwargs)
        c = ProductCategory.objects.get(slug=self.kwargs['category_slug'])
        con = self.get_user_context(
            title='Категория - ' + str(c.name),
            cat_selected=c.pk
        )
        return dict(list(context.items()) + list(con.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    """Страница добавление поста"""
    form_class = AddFormPost
    template_name = 'blogsushi/addpost.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'
    # raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Добавить пост')
        return dict(list(context.items())+list(con.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = FormUser
    template_name = 'blogsushi/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Регистрация')
        return dict(list(context.items())+list(con.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'blogsushi/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        con = self.get_user_context(title='Авторизация')
        return dict(list(context.items())+list(con.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')




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


def page_not_found(request, exсeption):
    return HttpResponseNotFound('Страница не найдена')
