from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from libreria.forms import AuthorForm, GenreForm
from libreria.models import Book, Author, Order, Genre


# @login_required(login_url='/admin/login/')
def hello(request):
    return HttpResponse("HelloWorld!")


def book_list(request):
    return render(request, "book_list.html", {'books': Book.objects.all()})


def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        book = None

    return render(request,
                  "book_detail.html",
                  {
                      'book': book,
                      'book_id': book_id
                  })


@login_required(login_url='/admin/login/')
def orders(request):
    orders = Order.objects.filter(customer=request.user)
    return render(
        request, "orders.html",
        {"user": request.user, "orders": orders}
    )


def author_create(request):
    if request.method == "POST":
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            newAuthor = Author(name=author_form.cleaned_data['author_name'],
                               surname=author_form.cleaned_data['author_surname'])
            newAuthor.save()
            return HttpResponse("Author saved!!")
    else:
        author_form = AuthorForm()

    return render(request, "author_create.html", {"form": author_form})


def genre_create(request):
    if request.method == 'POST':
        genre_form = GenreForm(request.POST)
        if genre_form.is_valid():
            genre = Genre()
            genre.name = genre_form.cleaned_data['genre_name']
            genre.description = genre_form.cleaned_data['genre_description']
            genre.save()
        return HttpResponse("Genre saved!!")
    else:
        genre_form = GenreForm()

    return render(
        request,
        "genre_create.html",
        {'form': genre_form}
    )
