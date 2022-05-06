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

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "description",
            "price",
            "get_image",
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

    class Meta:
        model = Order
        fields = (
            "id",
            "customer",
            "complete",
            "orderItems",
            "state",
            "city",
            "address",
        )

class OrdersSerializer(serializers.ModelSerializer):    
    orderItems = OrderItemsSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "complete",
            "orderItems",
            "state",
            "city",
            "address",
        )

class CustomersSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Customer
        fields = (
            # "user",
            'first_name',
            'last_name',
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

class MyOrderItemsSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = OrderItem
        fields = (
            "book",
            "order",
            "quantity",
            "date_added",
        )

class MyOrdersSerializer(serializers.ModelSerializer):    
    orderItems = MyOrderItemsSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "user",
            "complete",
            "orderItems",
            "state",
            "city",
            "address",
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

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "orders",
        )



