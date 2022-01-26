from django import forms
from .models import Product, ProductCategory


class AddFormPost(forms.Form):
    title = forms.CharField(max_length=120, label='Заголовок')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Текст')
    # image = forms.ImageField()
    is_published = forms.BooleanField(label='Публикация')
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), label='Категория' , empty_label='Категория не выбрана')
