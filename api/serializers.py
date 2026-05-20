from rest_framework import serializers
from rest_framework.reverse import reverse

from base.models import Product, Category
from base.Serializers import (UserPublicSerializer,
                              CategoryPublicSerializer)

from .validators import (validate_price,
                         validate_caption,
                         unique_title_validator)


class ProductSerializer(serializers.ModelSerializer):

    name = serializers.CharField(validators=[unique_title_validator])
    link = serializers.SerializerMethodField(read_only=True)
    related_products = serializers.SerializerMethodField(read_only=True)
    is_approved = serializers.BooleanField(read_only=True)
    caption = serializers.CharField(
        allow_blank=True, validators=[validate_caption])

    image = serializers.ImageField(required=False, allow_null=True)

    price = serializers.DecimalField(max_digits=10, decimal_places=2,
                                     validators=[validate_price])
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True
    )
    category_data = CategoryPublicSerializer(source='category',
                                             read_only=True)

    user = UserPublicSerializer(source='seller', read_only=True)

    class Meta:
        model = Product
        fields = [
            'name',
            'link',
            'id',
            'price',
            'added',
            'updated',
            'caption',
            'is_approved',
            'image',
            'category',
            'category_data',
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

    def validate(self, attrs):

        name = attrs.get('name')
        caption = attrs.get('caption')

        if name and caption and name.lower() == caption.lower():
            raise serializers.ValidationError({
                "caption": "Caption and Title cannot be the same"
            })
        return attrs


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
