from rest_framework import serializers

from base.models import Product


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
