from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from os import sep
from django.conf import settings as config


# Error Views
def custom_page_not_found_view(request, exception):
    return render(request, "error_pages/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "error_pages/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "error_pages/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "error_pages/400.html", {})

# Create your views here.
@login_required
def root(request):
    return render(request,'main.html')

# Media Views
@login_required
def media_output(request,app,base,image:str):
    try:
        ext = image.split(".")[-1]
        image = open(f"{config.BASE_DIR}{sep}{app}{sep}media{sep}{base}{sep}{image}",'rb').read()
    except:
        image = open(f"{config.BASE_DIR}{sep}core{sep}static{sep}assets{sep}placeholder.png",'rb').read()
        ext = 'png'
    return HttpResponse(image,content_type=f"image/{ext}")

@login_required
def qr_media_output(request,app,base,image):
    try:
        ext = image.split(".")[-1]
        image = open(f"{config.BASE_DIR}{sep}{app}{sep}media{sep}{base}{sep}qr{sep}{image}",'rb').read()
    except:
        image = open(f"{config.BASE_DIR}{sep}core{sep}static{sep}assets{sep}placeholder_qr.png",'rb').read()
        ext = 'png'
    return HttpResponse(image,content_type=f"image/{ext}")  