
from SElab4.models import User
from django.shortcuts import render
import requests

from rest_framework import viewsets
from rest_framework.response import Response

#TODO each user should be able to register, login, show and update their profiles

class API_gateway(viewsets.ViewSet):

    def user_request_type(self,request):
        req_type = request.data["type"]


        if req_type == "register":
            try:
                return self.register(request.data)
            except:
                #TODO  handle the more than 3 times req part

        elif req_type == "login":
            try:
                return self.login(request.data)
            except:
                #TODO  handle the more than 3 times req part

        elif req_type == "show":
            try:
                return self.show(request.data)
            except:
                #TODO  handle the more than 3 times req part

        elif req_type == "update":
            try:
                return self.update(request.data)
            except:
                #TODO  handle the more than 3 times req part


        else :
            return HttpResponse('Bad Request', status=400)





    def register(self,data):
        #TODO
    def login(self,data):
        #TODO
    def show(self,data):
        #TODO
    def update(self,data):
        #TODO








