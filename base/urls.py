from django.urls import path
from . import  views

urlpatterns = [

    path('', views.home, name='home'),
    path('product/<uuid:id>/', views.product_detail, name='product_detail'),
    path('toggle-like/<uuid:id>/', views.toggle_like, name='toggle_like'),
    path('replies/<uuid:id>/', views.comment_replies, name='comment_replies'),
    path('post_ad/', views.post_ad, name='post_ad'),
    path('edit_ad/<uuid:id>', views.edit_ad, name='edit_ad'),

]