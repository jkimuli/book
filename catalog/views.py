from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from .models import Book,BookOrderInstance,Borrower

# Create your views here.

class BookListView(ListView):
    '''
     Returns a list of all books in the database
    '''
    model = Book 
    template_name = 'catalog/book/list.html'
    context_object_name = 'books'
    paginate_by = 10

class BookDetailView(DetailView):
    '''
    Returns the detailed overview of a specific book instance
    '''
    model = Book
    context_object_name = 'book'
    template_name = 'catalog/book/detail.html'

class BookUpdateView(UpdateView):
    '''
    Updates a given instance of a book object
    '''

    model = Book
    template_name= 'catalog/book/update.html'
    fields = ['title','summary','author','isbn','genres','image']
    success_url = reverse_lazy('catalog:book_list')


class BookDeleteView(DeleteView):
    '''
      Deletes a given instance of a book object
    '''

    pass

class BorrowerCreateView(CreateView):
    model = Borrower
    template_name = 'catalog/borrower/create.html'
    fields = ['first_name','last_name','email','gender','address','phone_number',
              'alternate_phone_number']
    success_url = reverse_lazy('catalog:book_list')


class BookOrderListView(ListView):
    model = BookOrderInstance
    template_name = 'catalog/bookorder/list.html'
    context_object_name = 'orders'

class BookOrderCreateView(CreateView):
    model = BookOrderInstance
    template_name = 'catalog/bookorder/create.html'
    fields = ['book','borrower']
    success_url = reverse_lazy('catalog:order_list')    



