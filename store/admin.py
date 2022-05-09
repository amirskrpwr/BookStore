from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
