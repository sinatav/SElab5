
from SElab4.models import User
from django.shortcuts import render
import requests
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

import hashlib

#TODO each user should be able to register, login, show and update their profiles



class Register(viewsets.ViewSet):



class Login(viewsets.ViewSet):




class Show(viewsets.ViewSet):




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








