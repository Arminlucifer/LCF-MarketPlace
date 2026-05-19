from rest_framework import serializers
from rest_framework.reverse import reverse

from base.models import Product, Category
from base.Serializers import (UserPublicSerializer,
                              CategoryPublicSerializer)


class ProductSerializer(serializers.ModelSerializer):

    link = serializers.SerializerMethodField(read_only=True)
    related_products = serializers.SerializerMethodField(read_only=True)

    user = UserPublicSerializer(source='seller', read_only=True)
    category = CategoryPublicSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'link',
            'id',
            'name',
            'price',
            'added',
            'updated',
            'is_approved',
            'image',
            'category',
            'user',
            'related_products',
        ]

    def get_link(self, obj):
        request = self.context.get('request')

        print(self.context)

        if request is None:
            return None

        return reverse('product-detail', kwargs={'pk': obj.id}, request=request)

    def get_related_products(self, obj):
        if not obj.category:
            return []

        qs = Product.objects.filter(category=obj.category).exclude(id=obj.id)

        random_products = qs.order_by('?')[:5]

        return OtherProducts(random_products, many=True, context=self.context).data


class OtherProducts(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    price = serializers.DecimalField(max_digits=10, decimal_places=2,
                                     read_only=True)
    seller = serializers.CharField(read_only=True)
    image = serializers.ImageField(read_only=True)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'pk',
            'name',
            'photo',
        ]
