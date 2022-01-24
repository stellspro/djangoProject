from django.urls import path
from .views import index, cats

urlpatterns = [
    path('', index),
    path('cats/<int:number>/', cats)
]
