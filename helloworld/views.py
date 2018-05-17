from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.db import models

from helloworld.forms import AuthorForm, GenreForm
from helloworld.models import Book, Author, Order, Genre


@login_required(login_url='/admin/login/')
def hello(request):
    return HttpResponse("HelloWorld!")


def bookList(request):
    return render(request, "bookList.html", {'books': Book.objects.all()})


def bookDetail(request, bookId):
    try:
        book = Book.objects.get(pk=bookId)
    except Book.DoesNotExist:
        book = None

    return render(request,
                  "bookDetail.html",
                  {
                      'book': book,
                      'bookId': bookId
                  })


@login_required(login_url='/admin/login/')
def orders(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, "orders.html", {"user": request.user, "orders": orders})


def authorCreate(request):
    if request.method == "POST":
        authorForm = AuthorForm(request.POST)
        if authorForm.is_valid():
            newAuthor = Author(name=authorForm.cleaned_data['author_name'],
                               surname=authorForm.cleaned_data['author_surname'])
            newAuthor.save()
            return HttpResponse("Author saved!!")
    else:
        authorForm = AuthorForm()

    return render(request, "authorCreate.html", {"form": authorForm})


def genreCreate(request):
    if request.method == 'POST':
        genreForm = GenreForm(request.POST)
        if genreForm.is_valid():
            genre = Genre()
            genre.name = genreForm.cleaned_data['genre_name']
            genre.description = genreForm.cleaned_data['genre_description']
            genre.save()
        return HttpResponse("Genre saved!!")
    else:
        genreForm = GenreForm()

    return render(request, "genreCreate.html", {'form': genreForm})
