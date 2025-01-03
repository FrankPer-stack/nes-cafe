from django.urls import path
from . import views

app_name = 'directive'

urlpatterns = [
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('coffee_presentation/', views.presentation, name='presentation'),
    path('', views.index, name='index'),
]
