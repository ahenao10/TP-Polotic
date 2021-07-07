from django.urls import path
from . import views

app_name = 'USUARIO'
urlpatterns = [
    path('layout', views.layout, name='layout'),
    path('', views.home, name='home'),
    path('registro', views.registro, name="registro"),
    path('buscar', views.buscar, name="buscar"),
    path('categories', views.categories, name="categories"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('category1', views.category1, name="category1"),
    path('category2', views.category2, name="category2"),
    path('category3', views.category3, name="category3"),
    path('product1', views.product1, name="product1"),
    path('product2', views.product2, name="product2"),
    path('product3', views.product3, name="product3"),
    path('product4', views.product4, name="product4"),
    path('product5', views.product5, name="product5"),
    path('product6', views.product6, name="product6"),
    path('product7', views.product7, name="product7"),
    path('product8', views.product8, name="product8"),
    path('product9', views.product9, name="product9"),
    path('product10', views.product10, name="product10"),
]