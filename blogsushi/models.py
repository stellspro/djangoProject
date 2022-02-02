from django.db import models


# Create your models here.
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name='Заголовок статьи')
    slug = models.SlugField(max_length=120, unique=True, db_index=True, verbose_name='Url')
    content = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    edited = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductCategory(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    slug = models.SlugField(max_length=120, unique=True, db_index=True, verbose_name='Url')
    description = models.CharField(max_length=120, verbose_name='Описание')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории продуктов'
