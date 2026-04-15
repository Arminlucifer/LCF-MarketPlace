from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from . models import Category, Product, Comment
from datetime import timedelta
from django.utils import timezone










def home(request):

    products = Product.objects.all()
    product_count = Product.objects.count()
    now = timezone.now()

    products_data = []

    for product in products:
        time_diff = now - product.added
        upload_time_str = ''
        if time_diff < timedelta(minutes=1):
            upload_time_str = 'just now!'
        elif time_diff < timedelta(hours=1):
            minutes = int(time_diff.total_seconds() // 60)
            upload_time_str = f'{minutes} minutes ago!'
        elif time_diff < timedelta(days=1):
            hours = int(time_diff.total_seconds() // 3600)
            upload_time_str = f'{hours} hours ago!'
        elif time_diff < timedelta(days=7):
            days = int(time_diff.total_seconds() // 86400)
            upload_time_str = f'{days} days ago!'
        elif time_diff < timedelta(days=30):
            weeks = int(time_diff.total_seconds() // (7 * 86400))
            upload_time_str = f'{weeks} weeks ago!'
        elif time_diff < timedelta(days=365):
            months = int(time_diff.total_seconds() // (30 * 86400))
            upload_time_str = f'{months} months ago!'
        else:
            upload_time_str = f'{product.added}'

        products_data.append({'product': product, 'upload_time': upload_time_str})

    context = {'products_data': products_data, 'product_count': product_count}




    return render(request, 'base/home.html', context)




def product_detail(request, id):
    page = 'product_detail'
    product = get_object_or_404(Product, id=id)
    context = {'product': product, 'page': page}


    return render(request, 'base/product_detail.html', context)