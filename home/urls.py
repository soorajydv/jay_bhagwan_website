
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("sweets/<str:name>", views.category_products,name='category_products'),

    path('search/', views.search_products, name='search_products'),
]
