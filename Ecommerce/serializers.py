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


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name','price']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model= OrderItem
        fields = ["customer_id","product_id","quantity"]
class CartDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= OrderItem
        fields = ["quantity"]

class OrderSerializer(serializers.ModelSerializer):
    # product = serializers.SerializerMethodField("get_values")
    # quantity = CartDetailsSerializer(read_only=True,many=True)
    
    class Meta:
        model = Order
        fields ="__all__"
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     print("lll",representation)
    #     id=representation['orderitem_id']
    #     representation['product'] = instance.orderitem_id.values()
    #     return representation

  

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'