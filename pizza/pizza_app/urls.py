"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import index_page, about_page, store_page, product_page, pizza_choice, order_page, remove_pizza_chose
urlpatterns = [
    path('', index_page, name="index"),
    path('about', about_page, name="about"),
    path('store', store_page, name="store"),
    path('product', product_page, name="product"),
    path('choice', pizza_choice, name="pizza_choice"),
    path('order', order_page, name="order"),
    path('remove', remove_pizza_chose, name="remove"),
]
