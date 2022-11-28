from rest_framework import serializers
from Ecommerce.models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "name","address","phone","email","password"
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model= OrderItem
        fields = ["customer_id","product_id","quantity"]
        # depth=1

   