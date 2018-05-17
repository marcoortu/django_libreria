from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.db.models import permalink
from django.urls import reverse
import datetime


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.surname)


class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    genre = models.ForeignKey(Genre)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Order(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now)
    customer = models.ForeignKey(User)
    books = models.ManyToManyField(Book)

    def __unicode__(self):
        return "%s: %s #items(%d)" % (self.customer, self.date, self.books.count())


class OrderAdmin(admin.ModelAdmin):
    exclude = ['date', 'customer']

    def save_model(self, request, obj, form, change):
        obj.customer = request.user
        super(OrderAdmin, self).save_model(request, obj, form, change)
