from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics, mixins
from rest_framework.filters import (SearchFilter,
                                    OrderingFilter)
from rest_framework.parsers import MultiPartParser, FormParser


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
    # select_related pulls seller + category in the same SQL query (JOIN)
    # instead of one extra query per product for each nested relation.
    # Without this, ProductSerializer's nested `user` and `category_data`
    # fields each triggered a separate DB hit per row (classic N+1).
    parser_classes = [MultiPartParser, FormParser]
    queryset = Product.objects.select_related('seller', 'category').all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter,
                       OrderingFilter]

    search_fields = ['name', 'category__name',
                     'seller__name', 'seller__username']
    ordering_fields = ['price', 'added', 'name']

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(seller=user)


class ProductRetrieveUpdateDestroyAPIView(
        generics.RetrieveUpdateDestroyAPIView):

    staff_perm = True

    queryset = Product.objects.select_related('seller', 'category').all()
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


class VendorDashboardProductAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [
        IsOwnerOrReadOnly |
        StaffProductEditor]

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Product.objects.none()

        return Product.objects.select_related('seller', 'category').filter(seller=user)

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)
