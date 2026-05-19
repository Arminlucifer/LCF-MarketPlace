from django.urls import path

from . views import (ProductListCreateAPIView,
                     ProductRetrieveUpdateDestroyAPIView,)

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<uuid:pk>', ProductRetrieveUpdateDestroyAPIView.as_view()),
]
