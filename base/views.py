from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def homepage(request):

    #check to see if user is logging in
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        #Authenticate user
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("homepage")
        
        else:
            messages.error(request, "Incorrect Username or Password")
            return redirect("homepage")

    name = "Nsikan Yakmfiok Essien"
    return render(request, "base/index.html", {'name':name})

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("homepage")

def register_user(request):

    return render(request, "base/register.html")

