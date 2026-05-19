from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse

from base.models import Product


def get_products(request):
    products = Product.objects.all().first()

    data = model_to_dict(products, fields=['id', 'name', 'price'])
    return JsonResponse(data)
