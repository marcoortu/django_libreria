import unittest

from django.test import TestCase, Client

from libreria.models import *


class ModelTest(TestCase):
    def setUp(self):
        self.user = User(username="admin", email="email@email.com", password="administrator")

        self.user.save()

        horror = Genre(name="Horror", description="Horror")
        horror.save()
        fantasy = Genre(name="fantasy", description="fantasy")
        fantasy.save()

        martin = Author(name="George Raymond Richard", surname="Martin")
        martin.save()

        gameOfThrones = Book(title="a game of throne", genre=fantasy, author=martin)
        gameOfThrones.save()

    def testFindModels(self):
        self.assertEqual(len(Genre.objects.all()), 2)
        self.assertEqual(len(Author.objects.all()), 1)
        self.assertEqual(len(Book.objects.all()), 1)

    def testFindUser(self):
        self.assertEquals(len(User.objects.all()), 1)


class ViewsTest(TestCase):
    def setUp(self):
        self.user = User(username="admin", email="email@email.com", password="administrator")

        self.user.save()

        horror = Genre(name="Horror", description="Horror")
        horror.save()
        fantasy = Genre(name="fantasy", description="fantasy")
        fantasy.save()

        martin = Author(name="George Raymond Richard", surname="Martin")
        martin.save()

        gameOfThrones = Book(title="a game of throne", genre=fantasy, author=martin)
        gameOfThrones.save()

        self.adminPassowrd = "administrator"
        self.adminUsername = "administrator"
        self.user = User.objects.create_user(username=self.adminUsername, email="email@email.com",
                                             password=self.adminPassowrd)
        self.client = Client()
        self.client.logout()

    def testHelloWorldView(self):
        response = self.client.login(username=self.user.username, password=self.adminPassowrd)
        self.assertTrue(response)
        response = self.client.get('/hello', follow=True)
        self.assertContains(response, 'HelloWorld!')

    def testOrdersView(self):
        response = self.client.login(username=self.user.username, password=self.adminPassowrd)
        self.assertTrue(response)
        response = self.client.get('/orders', follow=True)
        orders = Order.objects.filter(customer=self.user)
        self.assertContains(response, orders.count())

    def testOrdersNotLoggedView(self):
        response = self.client.get('/orders/')
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/admin/login/?next=/orders/')

    def testBookList(self):
        response = self.client.get('/books', follow=True)
        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)


if __name__ == "__main__":
    unittest.main()
