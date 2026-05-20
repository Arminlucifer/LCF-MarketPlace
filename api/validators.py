from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from base.models import Product


def validate_price(price):
    if price <= 0:
        raise serializers.ValidationError(
            f'Product Price Must Be Greater Than 0, You enterted {price}')
    return price


def validate_caption(data):
    pass


# def validate_title(title):
#     if title is None:
#         raise serializers.ValidationError("The title cannot be empty")
#     if Product.objects.filter(name__iexact=title):
#         raise serializers.ValidationError(
#             'Product With This name already exists')
#     return title

unique_title_validator = UniqueValidator(
    queryset=Product.objects.all(), lookup='iexact')
