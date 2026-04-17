from django.urls import path
from . import  views

urlpatterns = [

    path('', views.home, name='home'),
    path('product/<uuid:id>/', views.product_detail, name='product_detail'),
    path('toggle-like/<uuid:id>/', views.toggle_like, name='toggle_like'),
    path('replies/<uuid:id>/', views.comment_replies, name='comment_replies'),

]