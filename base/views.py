from django.shortcuts import render, redirect
from account.models import User









def home(request):
    return render(request, 'base/home.html')