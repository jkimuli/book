from django.db import models
from django.urls import reverse
from datetime import datetime,timedelta
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    '''
    Model representing a book genre eg Science Fiction,Thriller
    '''
    name = models.CharField(max_length=200,help_text='Enter a book genre')

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

        return '%s, %s' % (self.first_name,self.last_name)


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

    def get_absolute_url(self):

        # return url for the instance of Borrower

        return reverse('borrower_detail',args=[str(self.id)])

    def __str__(self):

        return '%s  %s' % (self.first_name,self.last_name)


class Book(models.Model):

    """
     Model representing a given book 

    """

    LOAN_STATUS = (

        ('o','Loaned Out'),
        ('a', 'Available')
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name='author_books')
    summary = models.TextField(max_length=1000,help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN',max_length=13,help_text='13-character ISBN number for the book',default='0000000000000')
    genres = models.ManyToManyField(Genre,help_text='Select genres for this book',related_name='genre_books')
    #status = models.CharField(max_length=1,choices=LOAN_STATUS,default='a',help_text='Book Availability status')
    is_available = models.BooleanField(default=True)
    image = models.FileField(blank=True,upload_to='book_images/',default='book_images/book.png')

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

        return reverse('book_detail', args=[str(self.id)])

    def display_genre(self):

        '''
          Return the genres specified for a given book as a string

        '''

        return ', '.join([genre.name for genre in self.genre.all()])

    display_genre.short_description = 'Genres'


class BookOrderInstance(models.Model):

    '''
    Model representing when a specific book is loaned out -- tracking book rentals

    '''

    def default_due_date():
        # default due date 90 days from creation date

        return datetime.now() + timedelta(90)

    book = models.ForeignKey(Book,help_text='Enter book to be lent out')
    borrower = models.ForeignKey(Borrower,help_text='Enter name of person borrowing book')
    loaned_out_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True,default=default_due_date)
    is_returned = models.BooleanField(default=False,help_text='Mark a book as returned')
    return_date = models.DateField(blank=True,null=True)

    def get_absolute_url(self):

        return reverse('order_detail',args=[str(self.id)])

    def __str__(self):

        return 'Book- %s, borrowed by %s on %s' % (self.book,self.borrower,self.loaned_out_date)

    def save(self,*args,**kwargs):

        # update the availability status of book that has been lent

        super(BookOrderInstance,self).save(*args,**kwargs)

        if self.pk and  not self.is_returned:

            # if book order is created and is_returned==False, set book status to not available

            lent_book = self.book
            lent_book.is_available = False

            #update book in Book Model 
            lent_book.save()

        else:

            lent_book = self.book
            lent_book.is_available = True
            lent_book.save()

    @property
    def return_date_over_due(self):

        ''''
        Return whether a book return is overdue dependent upon the due date specified

        '''

        overdue_status = ''

        if datetime.today().date > self.due_date:
            overdue_status = 'Book Return Overdue'
        else:
            overdue_status = 'Not yet overdue'

        return overdue_status

            

   


