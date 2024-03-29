"""MicroServiceArch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from MicroServiceArch.SElab4.display import APIGateway, Register, Login, Show, SeeBooks
from MicroServiceArch.Books.display import BookGateway, Create, Update, Read, Delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/main/', APIGateway.as_view({'post': 'user_request_type'})),
    path('api/register/', Register.as_view({'post': 'user_request_type'})),
    path('api/login/', Login.as_view({'post': 'user_request_type'})),
    path('api/profile/', Show.as_view({'post': 'user_request_type'})),
    path('api/see-book/', SeeBooks.as_view({'post': 'user_request_type'})),
    path('api/main-book/', BookGateway.as_view({'post': 'user_request_type'})),
    path('api/create-book/', Create.as_view({'post': 'user_request_type'})),
    path('api/update-book/', Update.as_view({'post': 'user_request_type'})),
    path('api/read-book/', Read.as_view({'post': 'user_request_type'})),
    path('api/delete-book/', Delete.as_view({'post': 'user_request_type'})),
]
