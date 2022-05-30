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
    path("users/current_user", views.current_user, name='current_user'),
    path('order_list/', views.OrderList.as_view(), name="order_list"),
    path('order_item_list/', views.OrderItemList.as_view(), name="order_item_list"),
    path('customer_list/', views.CustomerList.as_view(), name="customer_list"),
    path('author_list/', views.AuthorList.as_view(), name="author_list"),
    path('authors/<slug:author_slug>/', views.AuthorDetail.as_view()),
    path('illustrator_list/', views.IllustratorList.as_view(), name="illustrator_list"),
    path('illustrators/<slug:illustrator_slug>/', views.IllustratorDetail.as_view()),
    path('publisher_list/', views.PublisherList.as_view(), name="publisher_list"),
    path('publishers/<slug:publisher_slug>/', views.PublisherDetail.as_view()),
]
