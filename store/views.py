from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from django.db.models import Q

from .models import *

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

class ShippingAddressList(APIView):
    def get(self, request, format=None):
        shippingAddresses = ShippingAddress.objects.all()
        serializer = ShippingAddressesSerializer(shippingAddresses, many=True)
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
