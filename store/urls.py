from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.BookList.as_view(), name="book_list"),
    path('category_list/', views.CategoryList.as_view(), name="category_list"),
    path('books/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('books/<slug:category_slug>/<slug:book_slug>/', views.BookDetail.as_view()),
    path("books/search", views.search, name="search"),
    path("orders/", views.MyOrderList.as_view(), name="orders"),
    path("checkout/", views.checkout, name='checkout'),
    path('order_list/', views.OrderList.as_view(), name="order_list"),
    path('order_item_list/', views.OrderItemList.as_view(), name="order_item_list"),
    path('customer_list/', views.CustomerList.as_view(), name="customer_list"),
]
