# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-09 08:13
from __future__ import unicode_literals

import catalog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
                ('isbn', models.CharField(default='0000000000000', help_text='13-character ISBN number for the book', max_length=13, verbose_name='ISBN')),
                ('status', models.CharField(choices=[('o', 'On Loan'), ('a', 'Available')], default='d', help_text='Book Availability status', max_length=1)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Author')),
            ],
        ),
        migrations.CreateModel(
            name='BookOrderInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loaned_out_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(blank=True, default=catalog.models.BookOrderInstance.default_due_date)),
                ('book', models.ForeignKey(help_text='Enter book to be lent out', on_delete=django.db.models.deletion.CASCADE, to='catalog.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter first name', max_length=30)),
                ('last_name', models.CharField(help_text='Enter last name', max_length=30)),
                ('phone_number', models.CharField(help_text='Enter phone contact', max_length=30, verbose_name='Phone Number')),
                ('alternate_phone_number', models.CharField(blank=True, help_text='Enter alternate phone contact', max_length=30, null=True, verbose_name='Other Phone Number')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='bookorderinstance',
            name='borrower',
            field=models.ForeignKey(help_text='Enter name of person borrowing book', on_delete=django.db.models.deletion.CASCADE, to='catalog.Borrower'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Select genre for this book', on_delete=django.db.models.deletion.CASCADE, to='catalog.Genre'),
        ),
    ]
