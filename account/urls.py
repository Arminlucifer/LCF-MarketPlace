from django.urls import path
from . import views

urlpatterns = [

    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('register/',views.registeruser,name='register'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/settings/<str:username>', views.editprofile, name='editprofile')


]