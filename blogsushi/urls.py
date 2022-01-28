from django.urls import path
from .views import cats, IndexProduct, PostDetail

urlpatterns = [
    path('', IndexProduct.as_view(), name='home'),
    path('cats/<int:number>/', cats),
    path('post/<int:post_id>/', PostDetail.as_view(), name='post'),
    # path('add_post/', add_post, name='add_post')
]
