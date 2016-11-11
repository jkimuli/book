# Julius Kimuli - urls.py file for the catalog application

from django.conf.urls import url
from . import views

app_name = 'catalog'


urlpatterns = [

    url(r'^$',views.BookListView.as_view(),name='book_list'),
    url(r'^books/$',views.BookListView.as_view(),name='book_list'),

    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book_detail'),
    url(r'^book/edit/(?P<pk>\d+)$',views.BookUpdateView.as_view(),name='book_edit'),
    url(r'^book/delete/(?P<pk>\d+)$',views.BookDeleteView.as_view(),name='book_delete'),
    


]