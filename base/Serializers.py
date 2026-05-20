from rest_framework import serializers


class UserPublicSerializer(serializers.Serializer):
    id = serializers.BigIntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    avatar = serializers.ImageField(read_only=True)


class CategoryPublicSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    photo = serializers.SerializerMethodField(read_only=True)

    def get_photo(self, obj):

        if not obj.photo:
            return None

        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.photo.url)
        return obj.photo.url
