import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _

# Create your models here.
def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value) 

class Customer (models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True,blank=True)
    last_name = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return "Customer " + str(self.id)
    
       
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


class Author(models.Model):
    name = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    introduction = models.TextField(blank=True, null=True,)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/authors/{self.slug}/'

    @property
    def books(self):
        return self.book_set.all()

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''


class Publisher(models.Model):
    name = models.CharField(max_length=200, null=True)
    introduction = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/publishers/{self.slug}'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''


class Book(models.Model):
    name = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    language = models.CharField(max_length=200, null=True)
    translator = models.ForeignKey(Author, null=True, related_name="translations", blank=True, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    image = models.ImageField(null=True, blank=True)
    page_count = models.IntegerField(null=True, blank=True)
    publish_year = models.IntegerField(_('publish_year'), validators=[MinValueValidator(1290), max_value_current_year], null=True, blank=True)
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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=True, null=True, blank=False)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

        
    @property
    def orderItems(self):
        return self.orderitem_set.all()


class OrderItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

