from rest_framework import serializers

from base.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'price',
            'seller',
            'added',
            'is_approved',
            'image',
        ]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'pk',
            'name',
            'photo',
        ]
