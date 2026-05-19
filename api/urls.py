from django.urls import path

from . views import productlist

urlpatterns = [
    path('products/', productlist)
]
