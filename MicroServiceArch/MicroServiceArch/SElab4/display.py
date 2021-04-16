
from SElab4.models import User
from django.shortcuts import render
import requests

from rest_framework import viewsets
from rest_framework.response import Response

#TODO each user should be able to register, login, show and update their profiles