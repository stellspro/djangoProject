from django.db.models import Count

from .models import ProductCategory

menu = [{'name': 'Добавить статью', 'url_name': 'add_post'},
        ]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        category = ProductCategory.objects.annotate(Count('product'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)

        context['menu'] = user_menu
        context['category'] = category
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
