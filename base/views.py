from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):

    name = "Nsikan Yakmfiok Essien"
    return render(request, "base/index.html", {'name':name})
