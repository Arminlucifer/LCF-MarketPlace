from django.urls import path

from . views import (ProductListCreateAPIView,
                     ProductRetrieveUpdateDestroyAPIView,
                     CategoryMixinAPIView,
                     VendorDashboardProductAPIView)

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<uuid:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(),
         name = 'product-detail'),
    path('category', CategoryMixinAPIView.as_view()),
    path('category/<int:pk>', CategoryMixinAPIView.as_view()),
    path('dashboard/products/', VendorDashboardProductAPIView.as_view(),
         name = 'vendor-dashboard-products'),


]
