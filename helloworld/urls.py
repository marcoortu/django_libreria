"""helloworld URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from helloworld import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', views.hello),
    url(r'^books/', views.bookList),
    url(r'^book/(?P<bookId>\d+)/', views.bookDetail, name="book-detail"),
    url(r'^author/create', views.authorCreate, name="author-create"),
    url(r'^genre/create', views.genreCreate, name="genre-create"),
    url(r'^orders/', views.orders, name="orders"),
]
