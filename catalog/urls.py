# Julius Kimuli - urls.py file for the catalog application

from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^books/$',views.BookListView.as_view(),name='book_list'),


]