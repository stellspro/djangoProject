from django import template
from blogsushi.models import ProductCategory, Product


register = template.Library()


@register.inclusion_tag('blogsushi/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = ProductCategory.objects.all()
    else:
        cats = ProductCategory.objects.order_by(sort)
    return {'categories': cats, 'cat_selected': cat_selected}

