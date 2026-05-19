from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics, mixins

from .permissions import (IsOwnerOrReadOnly,
                          StaffProductEditor,)
from base.models import Product, Category
from .serializers import (ProductSerializer,
                          CategorySerializer,)


# def get_products(request):
#     products = Product.objects.all().first()

#     data = model_to_dict(products, fields=['id', 'name', 'price'])
#     return JsonResponse(data)


# @api_view(["GET", "POST"])
# def productlist(request, id=None):
#     if request.method == 'GET':
#         if id is not None:
#             obj = get_object_or_404(Product, id=id)
#             data = ProductSerializer(obj).data
#             return Response(data)

#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)
#     if request.method == "POST":
#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(seller=user)


class ProductRetrieveUpdateDestroyAPIView(
        generics.RetrieveUpdateDestroyAPIView):

    staff_perm = True

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly |
                          StaffProductEditor]


class CategoryMixinAPIView(generics.GenericAPIView,
                           mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.UpdateModelMixin):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
