from django.http import Http404
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import status, authentication,permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.
class BookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

class OrderList(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)
        
class OrderItemList(APIView):
    def get(self, request, format=None):
        orderItems = OrderItem.objects.all()
        serializer = OrderItemsSerializer(orderItems, many=True)
        return Response(serializer.data)

class CustomerList(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)

class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

class BookDetail(APIView):
    def get_object(self, category_slug, book_slug):
        try:
            return Book.objects.filter(category__slug=category_slug).get(slug=book_slug)
        except Book.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, book_slug, format=None):
        book = self.get_object(category_slug, book_slug)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get("query","")
    
    if query:
        books = Book.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response({"books":[]})

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    order = Order.objects.create(
        user = request.user,
        complete = request.data['complete'],
        state = request.data['state'],        
        city = request.data['city'],        
        address = request.data['address'],        
    )

    orderItems = []
    for item in request.data['orderItems']:
        orderItem = OrderItem.objects.create(
            book = Book.objects.get(id=item['book']['id']),
            order = order,
            quantity = item['quantity'],
        )
        orderItems.append(orderItem)

    return Response({"data":"Successfully added."}, status=status.HTTP_201_CREATED)


class MyOrderList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrdersSerializer(orders, many=True)
        return Response(serializer.data)