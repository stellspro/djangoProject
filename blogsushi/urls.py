from django.urls import path
from .views import IndexProduct, PostDetail, ShowCategories, AddPage

urlpatterns = [
    path('', IndexProduct.as_view(), name='home'),
    path('post/<slug:post_slug>/', PostDetail.as_view(), name='post'),
    path('category/<slug:category_slug>', ShowCategories.as_view(), name='category'),
    path('add_post/', AddPage.as_view(), name='add_post')
]
