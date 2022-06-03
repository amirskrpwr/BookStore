from django.http import Http404
from django.db.models import Q

from rest_framework import status, authentication,permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

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

class CustomerDetail(APIView):
    def get_object(self, user_id):
        try:
            return Customer.objects.get(user=user_id)
        except Customer.DoesNotExist:
            raise Http404
    
    def get(self, request, user_id, format=None):
        customer = self.get_object(user_id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

class AuthorList(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorsSerializer(authors, many=True)
        return Response(serializer.data)

class AuthorDetail(APIView):
    def get_object(self, author_slug):
        try:
            return Author.objects.get(slug=author_slug)
        except Author.DoesNotExist:
            raise Http404
    
    def get(self, request, author_slug, format=None):
        author = self.get_object(author_slug)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

class IllustratorList(APIView):
    def get(self, request, format=None):
        illustrators = Illustrator.objects.all()
        serializer = IllustratorsSerializer(illustrators, many=True)
        return Response(serializer.data)

class IllustratorDetail(APIView):
    def get_object(self, illustrator_slug):
        try:
            return Illustrator.objects.get(slug=illustrator_slug)
        except Illustrator.DoesNotExist:
            raise Http404
    
    def get(self, request, illustrator_slug, format=None):
        illustrator = self.get_object(illustrator_slug)
        serializer = IllustratorSerializer(illustrator)
        return Response(serializer.data)

class PublisherList(APIView):
    def get(self, request, format=None):
        publishers = Publisher.objects.all()
        serializer = PublishersSerializer(publishers, many=True)
        return Response(serializer.data)

class PublisherDetail(APIView):
    def get_object(self, publisher_slug):
        try:
            return Publisher.objects.get(slug=publisher_slug)
        except Publisher.DoesNotExist:
            raise Http404
    
    def get(self, request, publisher_slug, format=None):
        publisher = self.get_object(publisher_slug)
        serializer = PublisherSerializer(publisher)
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
        Book.objects.filter(id = item['book']['id']).update(count=item['book']['count']-item['quantity'])    
        

    return Response({"data":"Successfully added."}, status=status.HTTP_201_CREATED)


class MyOrderList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrdersSerializer(orders, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def current_user(request):
    user = request.user
    return Response({
        'username': user.username,
        'password': user.password,
        'email': user.email,
        'id':user.id
    })

# @api_view(['POST'])
# def customerModification(request, username):
#     customer, created = Customer.objects.update_or_create(
#         user= User.objects.get(id=request.data['user_id']),
#         defaults={
#             'birth_date': request.data['customer']['birth_date'],
#             'first_name': request.data['customer']['first_name'],
#             'last_name': request.data['customer']['last_name'],            
#             'image': request.data['image']
#         }
#     )
#     return Response({"data":"Successfully added."}, status=status.HTTP_201_CREATED)

class CustomerModification(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = CustomerSerializer(data=request.data)

        customer, created = Customer.objects.update_or_create(
            user = User.objects.get(id=request.data.get('user')),
            defaults={
                'birth_date': request.data.get('birth_date', None),
                'first_name': request.data.get('first_name', None),
                'last_name': request.data.get('last_name', None),                
                'image': request.data.get('image', None)
            }
        )

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
