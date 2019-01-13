# Julius Kimuli - urls.py file for the catalog application

from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'catalog'


urlpatterns = [

    path('',views.BookListView.as_view(),name='book_list'),
    path('books',views.BookListView.as_view(),name='book_list'),

    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('book/edit/<int:pk>',views.BookUpdateView.as_view(),name='book_edit'),
    path('book/delete/<int:pk>',views.BookDeleteView.as_view(),name='book_delete'),

    path('borrower/create', views.BorrowerCreateView.as_view(),name='borrower_create'),

    path('orders',views.BookOrderListView.as_view(),name='order_list'),
    path('order/create',views.BookOrderCreateView.as_view(),name='order_create'),
    


]