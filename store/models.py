from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer (models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True,blank=True)
    last_name = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return "Customer " + str(self.id)
        
    @property
    def orders(self):
        return self.order_set.all()

    # @property
    # def user(self):
    #     return self.user

    @property
    def shippingAddresses(self):
        return self.shippingaddress_set.all()

       
class Category(models.Model):
    name = models.CharField(max_length=255, )
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'

    @property
    def books(self):
        return self.book_set.all()


class Book(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ('-date_added',) 

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def __str__(self):
        return self.name

    @property
    def orderItems(self):
        return self.orderitem_set.all()

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=True, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for item in orderitems:
            if item.book.digital == False:
                shipping = True
        return shipping
        
    @property
    def orderItems(self):
        return self.orderitem_set.all()

    @property
    def shippingAddresses(self):
        return self.shippingaddress_set.all()


class OrderItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)



class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
        