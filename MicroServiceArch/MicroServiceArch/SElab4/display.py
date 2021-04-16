
from SElab4.models import User
from django.shortcuts import render
import requests
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

import hashlib
import datetime
import random
import string

#TODO each user should be able to register, login, show and update their profiles



class Register(viewsets.ViewSet):

    def user_request_type(self, request):
        user = User()
        data = request.data
        try:
            user.username = data['username']
            user.password =  hashlib.md5(data['password'].encode('utf-8')).digest()
            user.email= data['email']
            user.mobile = data['mobile']
            user.save()
           
        except KeyError:
            return HttpResponse('EMPTY_FIELDS', status=406)
        return HttpResponse('user registered successfully.', status=200)



class Login(viewsets.ViewSet):

    def user_request_type(self, request):
        try:
            username = request.data['username']
            password =   str(request.data['password'])

        except KeyError:
            return HttpResponse('EMPTY_FIELDS', status=406)
        user = User.objects.get(username=username)
        # check if the password is correct or not
        if str(user.password) == str(hashlib.md5(password.encode('utf-8')).digest()):
            t =  django.utils.timezone.now()
            if user.token_time > t:
                return HttpResponse(user.token, status=200)
            else:
                user.token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))
                user.token_exp_time = django.utils.timezone.now() + django.utils.timezone.timedelta(hours=1, minutes=30)
                user.save()
                return HttpResponse(user.token, status=200)
        else:
            return HttpResponse("NOT FOUND", status=404)




class Show(viewsets.ViewSet):

    def user_request_type(self, request):
        try:
            token = request.data['token']
        except KeyError:
            return HttpResponse('EMPTY_FIELDS', status=406)

        user = User.objects.get(token=token)
        t = django.utils.timezone.now()
        if user.token_exp_time < t
            return HttpResponse('Token expired', status=409)

        if 'show' in request.data:
            user.profile = request.data['show']
            user.save()

        return HttpResponse('profile: ' + user.profile, status=200)




class Update(viewsets.ViewSet):










initiate_values = {"register_count" :0, "login_counts" : 0, "show_counts" : 0, "update_counts" : 0}
class API_gateway(viewsets.ViewSet):

    def user_request_type(self,request):
        req_type = request.data["type"]


        if req_type == "register":
            try:
                return self.register(request.data)
            except:
               initiate_values['register_count'] += 1
               if self.is_request_timeout(initiate_values['register_count']):
                   print("REQUEST_TIMEOUT")


        elif req_type == "login":
            try:
                return self.login(request.data)
            except:
                initiate_values['login_count'] += 1
                if self.is_request_timeout(initiate_values['login_count']):
                    print("REQUEST_TIMEOUT")


        elif req_type == "show":
            try:
                return self.show(request.data)
            except:
                initiate_values['show_count'] += 1
                if self.is_request_timeout(initiate_values['show_count']):
                    print("REQUEST_TIMEOUT")

        elif req_type == "update":
            try:
                return self.update(request.data)
            except:
                initiate_values['update_count'] += 1
                if self.is_request_timeout(initiate_values['update_count']):
                    print("REQUEST_TIMEOUT")

        else :
            return HttpResponse('Bad Request', status=400)

    def set_response(self, data, url):
        response = requests.post(url, data=data)
        return HttpResponse(response.text, status=response.status_code)

    def is_request_timeout(self, request_count):
        if request_count >= 3:
            return True
        else:
            return False



    def register(self,data):
        url = 'http://127.0.0.1:8000/api/register'
        self.set_response(data, url)
    def login(self,data):
        url = 'http://127.0.0.1:8000/api/login'
        self.set_response(data, url)
    def show(self,data):
        url = 'http://127.0.0.1:8000/api/show'
        self.set_response(data, url)
    def update(self,data):
        url = 'http://127.0.0.1:8000/api/update'
        self.set_response(data, url)








