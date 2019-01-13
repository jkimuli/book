from django.db import models
from django.urls import reverse
from datetime import datetime,timedelta,date
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    '''
    Model representing a book genre eg Science Fiction,Thriller
    '''
    name = models.CharField(max_length=140,help_text='Enter a book genre')

    def __str__(self):

        ''''
        String representation of model instance

        '''
        return self.name


class Author(models.Model):

    ''' 
    Model representing a book Author

    '''

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def get_absolute_url(self):

        # return the url for a specific author instance 

        return reverse('author_detail', args=[str(self.id)])

    def __str__(self):

        '''
        String representation of author instance 

        '''

        return '%s  %s' % (self.first_name,self.last_name)


class Borrower(models.Model):
    '''
    Model representing a book Borrower
    '''

    GENDER = (
        ('M','Male'),
        ('F','Female')
    )

    first_name = models.CharField(max_length=30,help_text='Enter first name')
    last_name = models.CharField(max_length=30,help_text='Enter last name')
    phone_number = models.CharField(max_length=30,verbose_name="Phone Number",help_text='Enter phone contact')
    alternate_phone_number = models.CharField(max_length=30,verbose_name='Other Phone Number',blank=True,null=True,help_text="Enter alternate phone contact")
    address = models.CharField(max_length=100,blank=True,default= ' ',help_text='Enter the address of the borrower')
    gender = models.CharField(max_length=1,choices=GENDER,default='M',help_text='Enter the gender of the borrower')
    email = models.EmailField(max_length=254,help_text='Enter an email address for the borrower')

    def get_absolute_url(self):

        # return url for the instance of Borrower

        return reverse('borrower_detail',args=[str(self.id)])

    def __str__(self):

        return '%s  %s' % (self.first_name,self.last_name)


class Book(models.Model):

    """
     Model representing a given book 

    """

    title = models.CharField(max_length=140)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name='author_books')
    summary = models.TextField(max_length=1000,help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN',max_length=13,help_text='13-character ISBN number for the book',default='0000000000000')
    genres = models.ManyToManyField(Genre,help_text='Select genres for this book',related_name='genre_books')
    is_available = models.BooleanField(default=True,help_text='Availability status of a book',editable=False)
    image = models.ImageField(blank=True,upload_to='book_images/',default='book_images/book.png')
    

    def __str__(self):

        return self.title

    @property
    def status(self):

        status = ''
        if self.is_available:
            status = 'Available'
        else:
            status = 'Loaned Out'

        return status
   
    def get_absolute_url(self):

        return reverse('catalog:book_detail', args=[self.id])
    
    def display_genres(self):
        '''
          Return the genres specified for a given book as a string
        '''
        return ', '.join([genre.name for genre in self.genres.all()])

    display_genres.short_description = 'Genres'

class BookOrderInstance(models.Model):

    '''
    Model representing when a specific book is loaned out -- tracking book rentals

    '''

    def default_due_date():
        # default due date 90 days from creation date

        return datetime.now() + timedelta(90)

    book = models.ForeignKey(Book,on_delete=models.CASCADE,help_text='Enter book to be lent out',
                            limit_choices_to={'is_available':True})
    borrower = models.ForeignKey(Borrower,on_delete=models.CASCADE,help_text='Enter name of person borrowing book')
    loaned_out_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True,default=default_due_date,editable=False)
    is_returned = models.BooleanField(default=False,help_text='Mark a book as returned')
    return_date = models.DateField(blank=True,null=True,editable=False)

    class Meta:
        verbose_name_plural = "Book Orders"

    def get_absolute_url(self):

        return reverse('order_detail',args=[str(self.id)])

    def __str__(self):

        return 'Book- %s, borrowed by %s on %s' % (self.book,self.borrower,self.loaned_out_date)

    def save(self,*args,**kwargs):
        if self.pk and self.is_returned:
            #update return date now that the book has been returned
            self.return_date = datetime.today()
        super(BookOrderInstance,self).save(*args,**kwargs)      


    @property
    def return_date_overdue(self):

        ''''
        Return whether a book return is overdue dependent upon the due date specified
        '''
        overdue_status = 'Book already returned!'

        if not self.is_returned:
            if date.today() > self.due_date:
                overdue_status = 'Book Return Overdue'
            else:
                overdue_status = 'Not yet overdue'
        
        return overdue_status

            

   


