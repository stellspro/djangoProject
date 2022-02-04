from django.urls import path
from .views import IndexProduct, PostDetail, ShowCategories, AddPage, RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', IndexProduct.as_view(), name='home'),
    path('post/<slug:post_slug>/', PostDetail.as_view(), name='post'),
    path('category/<slug:category_slug>', ShowCategories.as_view(), name='category'),
    path('add_post/', AddPage.as_view(), name='add_post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')

]
