# https://www.programmersought.com/article/15446158742/
from datetime import datetime
from django.test import TestCase
from study_app.models import Author, Book, Publisher, AuthorDetail


class ORMTest(TestCase):
    def setUp(self):
        publisher1 = Publisher.objects.create(name='A 출판사', address='서울')
        publisher2 = Publisher.objects.create(name='B 출판사', address='부산')
        publisher3 = Publisher.objects.create(name='C 출판사', address='목포')

        book1 = Book.objects.create(title='파이썬 기초', price=111.12, publish_day=datetime(year=2018, month=1, day=1), publisher=publisher1)
        book2 = Book.objects.create(title='파이썬을 이용한 크롤링', price=222.34, publish_day=datetime(year=2020, month=6, day=26), publisher=publisher2)
        book3 = Book.objects.create(title='장고의 강력한 ORM 배우기', price=333.56, publish_day=datetime(year=2021, month=6, day=1), publisher=publisher3)

        author1 = Author.objects.create(name='철수')
        author1.author_detail = AuthorDetail.objects.create(city='서울', email='a@abc.dom')
        author1.save()

        author2 = Author.objects.create(name='영희')
        author2.author_detail = AuthorDetail.objects.create(city='부산', email='b@abc.dom')
        author2.save()

        author3 = Author.objects.create(name='영수')
        author3.author_detail = AuthorDetail.objects.create(city='목포', email='c@abc.dom')
        author3.save()

        author1.books.add(book1, book2)
        author2.books.add(book2, book3)
        author3.books.add(book1)

    def test_orm(self):
        print()
        books = Book.objects.filter(title__contains='파이썬')
        print("Book.objects.filter(title__contains='파이썬')")
        print(books, '\n')

        books = Book.objects.filter(publish_day__year=2020)
        print("Book.objects.filter(publish_day__year=2020)")
        print(books, '\n')

        books = Book.objects.filter(publish_day__month=6).values('title')
        print("Book.objects.filter(publish_day__month=6).values('title')")
        print(books, '\n')

        books = Book.objects.filter(price__gt=10)
        print("Book.objects.filter(price__gt=10)")
        print(books, '\n')

        books = Book.objects.filter(price__gt=10).values('title', 'price')
        print("Book.objects.filter(price__gt=10).values('title', 'price')")
        print(books, '\n')

        books = Book.objects.filter(title__isnull=True)
        print("Book.objects.filter(title__isnull=True)")
        print(books, '\n')

        books = Book.objects.filter(title__isnull=False)
        print("Book.objects.filter(title__isnull=False)")
        print(books, '\n')
