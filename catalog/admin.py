from django.contrib import admin
from .models import Book,Genre,Author,BookOrderInstance,Borrower

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','isbn','summary','status')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    pass

@admin.register(BookOrderInstance)
class BookOrderAdmin(admin.ModelAdmin):
    list_display = ('book','borrower','loaned_out_date','due_date','return_date','is_returned')


admin.site.index_title = 'Book Catalog Administration'
admin.site.site_header = "Book Catalog Administration"
admin.site.index_title = "Book Catalog Administration"
