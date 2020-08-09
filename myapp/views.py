from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def trial(request):
    return HttpResponse("<h1>Project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="rashmi"
    return render(request,"myapp/profile.html",{'name':name})

def contact(request):
    return render(request,"myapp/contact.html")

def signup(request):
    return render(request,"myapp/signup.html")