import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _
from django_countries.fields import CountryField

# Create your models here.
def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value) 

def upload_customer(instance, filename):
    return 'customers/{filename}'.format(filename=filename)

def upload_author(instance, filename):
    return 'authors/{filename}'.format(filename=filename)

def upload_illustrator(instance, filename):
    return 'illustrators/{filename}'.format(filename=filename)

def upload_book(instance, filename):
    return 'books/{filename}'.format(filename=filename)

def upload_publisher(instance, filename):
    return 'publishers/{filename}'.format(filename=filename)


class Customer (models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_customer, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True,blank=True)
    last_name = models.CharField(max_length=200, null=True,blank=True)

    def __str__(self):
        return "Customer " + str(self.id)

    def get_absolute_url(self):
        return f'/customers/{self.id}/'


    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
       
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
    country = CountryField(default="IR")
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=upload_author, null=True, blank=True)
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

    def get_flag(self):
        if self.country:
            return 'http://127.0.0.1:8000' + self.country.flag
        return ''


class Publisher(models.Model):
    name = models.CharField(max_length=200, null=True)
    introduction = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_publisher, null=True, blank=True)
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

class Illustrator(models.Model):
    name = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.CharField(max_length=200, null=True, blank=True)
    introduction = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_illustrator, null=True, blank=True)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/illustrator/{self.slug}'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

class Book(models.Model):
    name = models.CharField(max_length=200, null=True)
    count= models.IntegerField(null=True, blank=False)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    language = models.CharField(max_length=200, null=True)
    translator = models.ForeignKey(Author, null=True, blank=True, related_name="translations", on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)
    illustrator = models.ForeignKey(Illustrator, null=True, blank=True, related_name='books', on_delete=models.CASCADE)    
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    image = models.ImageField(upload_to=upload_book, null=True, blank=True)
    page_count = models.IntegerField(null=True, blank=True)
    publish_year = models.IntegerField(_('publish_year'), validators=[MinValueValidator(1290), max_value_current_year], null=True)
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
    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ('-date_added',) 

    def __str__(self):
        return str(self.id)

        
    @property
    def orderItems(self):
        return self.orderitem_set.all()


class OrderItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

