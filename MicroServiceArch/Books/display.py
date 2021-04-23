from MicroServiceArch.SElab4.models import User
from MicroServiceArch.Books.models import Book
import requests
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

import datetime


class CreateBook(viewsets.ViewSet):
    def user_request_type(self, request):
        data = request.data
        token = data['token']
        admin = User.objects.get(token=token, isAdmin=True)
        if not admin:
            return Response("no user or not admin")
        admin.token_generation_time = datetime.datetime.now()
        book = Book()
        book.title = data['title']
        book.author = data['author']
        book.category = data['category']
        book.save()
        return Response("Book Created Successfully!")


class UpdateBook(viewsets.ViewSet):
    def user_request_type(self, request):
        data = request.data
        token = data['token']
        admin = User.objects.get(token=token, isAdmin=True)
        if not admin:
            return Response("no user or not admin")
        admin.token_generation_time = datetime.datetime.now()
        book_id = data['id']
        book = Book.objects.get(book_id=book_id)
        if not book:
            return Response("Book id is Wrong!")
        else:
            if 'title' in data:
                book.username = data['title']
            if 'author' in data:
                book.mobile = data['author']
            if 'category' in data:
                book.password = data['category']
            book.save()
            return Response("Successfully updated")


class ReadBook(viewsets.ViewSet):
    def user_request_type(self, request):
        data = request.data
        token = data['token']
        admin = User.objects.get(token=token, isAdmin=True)
        if not admin:
            return Response("no user or not admin")
        admin.token_generation_time = datetime.datetime.now()
        book_id = data['id']
        book = Book.objects.get(book_id=book_id)
        if not book:
            return Response("Book id is Wrong!")
        else:
            return Response(
                "title : " + book.title + "\nauthor : " + book.author + "\ncategory : " + book.category)


class DeleteBook(viewsets.ViewSet):
    def user_request_type(self, request):
        data = request.data
        token = data['token']
        admin = User.objects.get(token=token, isAdmin=True)
        if not admin:
            return Response("no user or not admin")
        admin.token_generation_time = datetime.datetime.now()
        book_id = data['id']
        book = Book.objects.get(_id=book_id)
        if not book:
            return Response("not book")
        else:
            book.delete()
            return Response("deleted")


class BookGateway(viewsets.ViewSet):
    def user_request_type(self, request):
        type_req = request.data["type"]

        if type_req == 'create':
            return self.create(request.data)
        if type_req == 'update':
            return self.update(request.data)
        if type_req == 'read':
            return self.read(request.data)
        if type_req == 'delete':
            return self.delete(request.data)

        return HttpResponse('Bad Request', status=400)

    def set_response(self, data, url):
        response = requests.post(url, data=data)
        return Response(response.text)

    def create(self, data):
        url = 'http://127.0.0.1:8000/api/create'
        return self.set_response(data, url)

    def update(self, data):
        url = 'http://127.0.0.1:8000/api/update'
        return self.set_response(data, url)

    def read(self, data):
        url = 'http://127.0.0.1:8000/api/read'
        return self.set_response(data, url)

    def delete(self, data):
        url = 'http://127.0.0.1:8000/api/delete'
        return self.set_response(data, url)

