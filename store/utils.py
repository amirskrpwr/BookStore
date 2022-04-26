import json
from .models import *

def cookieCart (request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        
    items = []
    order = {'get_cart_items':0, 'get_cart_total':0, 'shipping':False}
    cartItems = order['get_cart_items']
    print('Cart:',cart)

    for i in cart:
        try:
            cartItems +=cart[i]["quantity"]
            book = Book.objects.get(id=i)
            total = book.price * cart[i]['quantity']

            order['get_cart_total'] += total 
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'book':{
                    'id':book.id,
                    'name':book.name,
                    'price':book.price,
                    'imageURL':book.imageURL,
                },
                'quantity':cart[i]['quantity'],
                'get_total':total
            }

            items.append(item)

            if (book.digital == False):
                order['shipping'] = True
        except:
            pass

    return {'cartItems': cartItems, 'order': order, 'items':items}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:        
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'items':items,'order':order,'cartItems':cartItems}


def guestOrder(request, data):
    print('User is not logged in..')
    print('COOKIES: ', request.COOKIES)

    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(email=email, )
    customer.name = name
    customer.save()

    order = Order.objects.create(customer=customer, complete=False)

    for item in items:
        book = Book.objects.get(id=item['book']['id'])
        orderItem = OrderItem.objects.create(Book=book, order=order, quantity=item['quantity'])

    return customer, order
