from pytz import country_names
from rest_framework import serializers

from django.contrib.auth.models import User
from django_countries.serializer_fields import CountryField
from .models import *

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "book",
            "order",
            "quantity",
        )

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "author",
            "language",
            "translator",
            "illustrator",
            "publisher",
            "slug",
            "description",
            "price",
            "count",
            "discount",
            "get_image",
            "page_count",
            "publish_year",
            "date_added",
            "get_absolute_url"
        )

    def to_representation(self, instance):
        rep = super(BooksSerializer, self).to_representation(instance)
        if instance.author:
            rep['author'] = [instance.author.name, '/authors/'+instance.author.slug]
        if instance.translator:
            rep['translator'] = [instance.translator.name, '/authors/'+instance.translator.slug]
        if instance.illustrator:
            rep['illustrator'] = [instance.illustrator.name, '/illustrators/'+instance.illustrator.slug]
        if instance.publisher:
            rep['publisher'] = [instance.publisher.name, '/publishers/'+instance.publisher.slug]
        if instance.category:
            rep['category'] = instance.category.name
        return rep

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
            "complete",
            "orderItems",
            "state",
            "city",
            "address",
            'date_added',
        )


class CustomersSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Customer
        fields = (
            "user",
            'first_name',
            'last_name',
        )

class BookSerializer(serializers.ModelSerializer):
    # orderItems = OrderItemsSerializer()

    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "author",
            "language",
            "translator",
            "illustrator",
            "publisher",
            "slug",
            "description",
            "price",
            "count",
            "discount",
            "get_image",
            "page_count",
            "publish_year",
            "date_added",
            "get_absolute_url"
        )

    def to_representation(self, instance):
        rep = super(BookSerializer, self).to_representation(instance)
        if (instance.author):
            rep['author'] = [instance.author.name, '/authors/'+instance.author.slug]
        if instance.translator:
            rep['translator'] = [instance.translator.name, '/authors/'+instance.translator.slug]
        if instance.illustrator:
            rep['illustrator'] = [instance.illustrator.name, '/illustrators/'+instance.illustrator.slug]
        rep['publisher'] = [instance.publisher.name, '/publishers/'+instance.publisher.slug]
        rep['category'] = instance.category.name
        return rep

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
            "date_added"
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

class CustomersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields =( 
            "id",
            "user",
            "image",
            "get_image",
            "first_name",
            "last_name",
            "birth_date",
        )
        
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            "id",
            "user",
            "image",
            "get_image",
            "first_name",
            "last_name",
            "birth_date",
        )


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Author
        fields = (
            'id',
            'name',
            'birth_date',
            'birth_place',
            'get_image',
            'introduction',
            'get_absolute_url'
        )

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    translations = BookSerializer(many=True)

    class Meta: 
        model= Author
        fields = [
            'id',
            'name',
            'birth_date',
            'birth_place',
            'get_image',
            'get_flag',
            'introduction',
            'books',
            'country',
            'translations',
            'get_absolute_url'
        ]
            
        
class IllustratorsSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Illustrator
        fields = (
            'id',
            'name',
            'birth_date',
            'birth_place',
            'get_image',
            'introduction',
            'get_absolute_url'
        )

class IllustratorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta: 
        model= Illustrator
        fields = (
            'id',
            'name',
            'birth_date',
            'birth_place',
            'get_image',
            'introduction',
            'books',
            'get_absolute_url'
        )

class PublishersSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Author
        fields = (
            'id',
            'name',
            'get_image',
            'introduction',
            'get_absolute_url'
        )

class PublisherSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta: 
        model= Author
        fields = (
            'id',
            'name',
            'get_image',
            'introduction',
            'books',
            'get_absolute_url'
        )
