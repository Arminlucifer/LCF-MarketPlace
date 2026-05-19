from rest_framework import serializers


class UserPublicSerializer(serializers.Serializer):
    id = serializers.BigIntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    avatar = serializers.ImageField(read_only=True)


class CategoryPublicSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    photo = serializers.ImageField(read_only=True)
