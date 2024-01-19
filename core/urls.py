from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    # Media URLS
    path('<app>/media/<base>/<image>',views.media_output,name='media_tab'),
    path('<app>/media/<base>/qr/<image>',views.qr_media_output,name='media_qr'),
    # ROOT
    path('',views.root,name="root_dashboard")
]