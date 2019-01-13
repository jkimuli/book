from django.db.models.signals import post_save
from django.dispatch import receiver

from catalog.models import BookOrderInstance

@receiver(post_save,sender=BookOrderInstance)
def update_availability_status(sender,**kwargs):
    # update availability status

    order = kwargs['instance'] # get book order that sent the post_save signal
    book = order.book # get book associated to this book order instance

    if order.pk and not order.is_returned:
        book.is_available = False
    else:
        book.is_available = True

    book.save()    
