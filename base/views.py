from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from . models import Category, Product, Comment









def home(request):
    products = Product.objects.all()
    context = {'products': products}

    return render(request, 'base/home.html', context)




def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {'product': product}

    return render(request, 'base/home.html', context)