from rest_framework import serializers
from django.contrib.auth.models import User
from bangazon_api.models import Store


class StoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class StoreSerializer(serializers.ModelSerializer):
    seller = StoreUserSerializer()
    is_favorite = serializers.BooleanField(required=False)

    class Meta:
        model = Store
        fields = ('id', 'name', 'description', 'seller', 'products', 'is_favorite')
        depth = 1


class AddStoreSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
