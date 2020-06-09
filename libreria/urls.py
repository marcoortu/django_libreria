"""libreria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from libreria import views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('books/', views.book_list),
    path('book/<int:book_id>/', views.book_detail, name="book-detail"),
    path('author/create', views.author_create, name="author-create"),
    path('genre/create', views.genre_create, name="genre-create"),
    path('orders/', views.orders, name="orders"),
]
