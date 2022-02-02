from django import forms
from .models import Product, ProductCategory


class AddFormPost(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Product
        fields = ['title', 'slug', 'content', 'is_published', 'image', 'category']
