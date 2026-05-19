from django.urls import path

from . views import (ProductListCreateAPIView,
                     ProductRetrieveUpdateDestroyAPIView,
                     CategoryMixinAPIView)

urlpatterns = [
    path('products', ProductListCreateAPIView.as_view()),
    path('products/<uuid:pk>', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('category', CategoryMixinAPIView.as_view()),
    path('category/<int:pk>', CategoryMixinAPIView.as_view()),


]
