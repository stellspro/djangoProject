from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name='Заголовок статьи')
    content = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(upload_to='images/', blank=True, verbose_name='Изображение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    edited = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductCategory(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    description = models.CharField(max_length=120, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории продуктов'
