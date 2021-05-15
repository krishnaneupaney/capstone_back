from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'product_image', 'price']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user






# class ProductSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     product_image = serializers.ImageField()
#     price = serializers.IntegerField()

#     # Create and return a new `Product` instance,
#     # given the validated data.
#     def create(self, validated_data):
#         return Product.objects.create(validated_data)

#     #Update and return an existing `Product` instance,
#     # given the validated data.

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.product_image = validated_data.get('product_image', instance.product_image)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.save()
    #     return instance
