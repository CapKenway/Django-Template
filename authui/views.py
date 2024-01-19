from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def ui_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request,'Wrong Username or Password')


    if request.user.is_authenticated:
        return redirect("/dashboard")
    else:
        return render(request,'sign-in.html')
    
def ui_logout(request):
    logout(request)
    return redirect('start_url')