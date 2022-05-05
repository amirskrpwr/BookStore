from rest_framework import serializers

from django.contrib.auth.models import User
from .models import *

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "book",
            "order",
            "quantity",
            "date_added",
        )

class ShippingAddressesSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ShippingAddress
        fields = (
            "customer",
            "order",
            "address",
            "city",
            "state",
            "zipcode",
            "date_added"
        )

class BooksSerializer(serializers.ModelSerializer):
    orderItems = OrderItemsSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "description",
            "price",
            "get_image",
            "orderItems",
            "get_absolute_url"
        )

class CategoriesSerializer(serializers.ModelSerializer):
    books = BooksSerializer(many=True)

    class Meta:
        model = Category
        field = (
            "id",
            "name",
            "get_absolute_url",
            "books"
        )

class OrdersSerializer(serializers.ModelSerializer):    
    orderItems = OrderItemsSerializer(many=True)
    shippingAddresses = ShippingAddressesSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "customer",
            "date_order",
            "complete",
            "transaction_id",
            "orderItems",
            "shipping",
            "shippingAddresses",
        )

class CustomersSerializer(serializers.ModelSerializer):    
    orders = OrdersSerializer(many=True)
    shippingAddresses = ShippingAddressesSerializer(many=True)
    

    class Meta:
        model = Customer
        fields = (
            # "user",
            'first_name',
            'last_name',
            "orders",
            "shippingAddresses"
        )

class BookSerializer(serializers.ModelSerializer):
    orderItems = OrderItemsSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "description",
            "price",
            "get_image",
            "orderItems",
            "get_absolute_url"
        )

class CategoriesSerializer(serializers.ModelSerializer):
    books = BooksSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "books",
            "get_absolute_url"
        )

class CategorySerializer(serializers.ModelSerializer):
    books = BooksSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "books",
            "get_absolute_url"
        )

class CustomerSerializer(serializers.ModelSerializer):
    orders = OrdersSerializer(many=True)
    shippingAddresss = ShippingAddressesSerializer(many=True)

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "orders",
            "shippingAddresses",
        )
      
