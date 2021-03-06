# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20161109_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(help_text='Select genres for this book', related_name='genre_books', to='catalog.Genre'),
        ),
        migrations.AddField(
            model_name='borrower',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', help_text='Enter the gender of the borrower', max_length=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, default='book_images/book.png', upload_to='book_images/'),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='address',
            field=models.CharField(blank=True, default=' ', help_text='Enter the address of the borrower', max_length=100),
        ),
    ]
