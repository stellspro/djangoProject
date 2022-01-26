from django.urls import path
from .views import index, cats, add_post

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:number>/', cats),
    path('add_post/', add_post, name='add_post')
]
