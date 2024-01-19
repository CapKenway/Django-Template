from django.contrib import admin
from django.urls import path, include
from authui import views

urlpatterns = [
    path('login',views.ui_login,name="ui-auth-login"),
    path('logout',views.ui_logout,name="ui-auth-logout")
]
