from django.urls import path
from . import views

urlpatterns = [
    path('categoriamenu/', views.CategoriaMenuListCreate.as_view(), name='categoriamenu-list'), 
    path('categoriamenu/<int:pk>/', views.CategoriaMenuDetail.as_view(), name='categoriamenu-detail'),
    path('mesas/', views.MenuListCreate.as_view(), name='mesas-list'),
    path('mesas/<int:pk>/', views.MenuDetail.as_view(), name='mesas-detail'),




]
