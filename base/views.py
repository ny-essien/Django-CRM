from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import UserRegistrationForm, AddRecordForm
from django.contrib.auth.models import User
from .models import Record 

# Create your views here.
def homepage(request):

    records = Record.objects.all()

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

    name = str(request.user).capitalize()
    context = {

        'name':name,
        'records':records
    }
    return render(request, "base/index.html", context)

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("homepage")

def register_user(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            if User.objects.filter(email = form.cleaned_data['email']):
                messages.error(request, "Email Address already exist")
                return redirect('register')
        
            form.save()

            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect("homepage")
            
    else:
        form = UserRegistrationForm()        
        context = {'form' : form }
        return render(request, 'base/register.html', context)
    
    return render(request, "base/register.html", {'form':form})


def customer_record(request, pk):

    if request.user.is_authenticated:
        #look up records
        customer_records = Record.objects.get(pk = pk)
        context = {

            'customer_records' : customer_records
        }
        return render(request, 'base/record.html', context )
    
    else:

        messages.error(request, "Log in to view page")
        return redirect("homepage")
    

def delete_record(request, pk):
    
    if request.user.is_authenticated:
        customer = Record.objects.get(pk = pk)
        customer.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('homepage')
    
    else:
        messages.error(request, 'You must be logged in to delete record')
        return redirect("homepage")
    

def add_record(request):

    page = "add"

    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect("homepage")
        context = {
            'form':form,
            'page':page,
        }     
        return render(request, 'base/add_record.html', context)
    
    else:
        messages.error(request, "Login required")
        return redirect("homepage")
    

def update_record(request, pk):

    page = "update"
    if request.user.is_authenticated:
        current_record = Record.objects.get(pk = pk)
        form = AddRecordForm(request.POST or None, instance= current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated")
            return redirect("homepage")
        context = {

            'form':form,
            'page': page,
            'current_record' :current_record
        }
        return render(request, "base/add_record.html", context)
    
    else:

        messages.error(request, "Login Required")
        return redirect("homepage")
    
    

