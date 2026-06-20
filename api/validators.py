from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from base.models import Product


def validate_price(price):
    if price <= 0:
        raise serializers.ValidationError(
            f'Product Price Must Be Greater Than 0, You enterted {price}')
    return price


def validate_caption(value):
    if value and not value.strip():
        raise serializers.ValidationError(
            'Caption cannot be blank or only whitespace.')
    if value and len(value) > 100:
        raise serializers.ValidationError(
            f'Caption must be 100 characters or fewer, got {len(value)}.')
    return value


# def validate_title(title):
#     if title is None:
#         raise serializers.ValidationError("The title cannot be empty")
#     if Product.objects.filter(name__iexact=title):
#         raise serializers.ValidationError(
#             'Product With This name already exists')
#     return title

unique_title_validator = UniqueValidator(
    queryset=Product.objects.all(), lookup='iexact')
