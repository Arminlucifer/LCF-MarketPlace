from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from base.models import Product
from .serializers import ProductSerializer

# def get_products(request):
#     products = Product.objects.all().first()

#     data = model_to_dict(products, fields=['id', 'name', 'price'])
#     return JsonResponse(data)


@api_view(["GET", "POST"])
def productlist(request, id=None):
    if request.method == 'GET':
        if id is not None:
            obj = get_object_or_404(Product, id=id)
            data = ProductSerializer(obj).data
            return Response(data)

        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
