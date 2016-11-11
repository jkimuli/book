from django.contrib import admin
from .models import Book,Genre,Author,BookOrderInstance,Borrower

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','isbn','summary','status','image','display_genres')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name',)
    search_fields = ('first_name','last_name',)

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone_number','alternate_phone_number','gender','address')
    search_fields = ('first_name','last_name','gender')
    list_filter = ('gender',)

@admin.register(BookOrderInstance)
class BookOrderAdmin(admin.ModelAdmin):
    list_display = ('book','borrower','loaned_out_date','due_date','return_date','is_returned')


admin.site.index_title = 'Book Catalog Administration'
admin.site.site_header = "Book Catalog Administration"
admin.site.index_title = "Book Catalog Administration"
