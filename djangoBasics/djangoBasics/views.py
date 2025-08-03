from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello World you are at homepage")
    return render(request, 'index.html')

def about(request):
    #return HttpResponse("Hello World you are at about page")
    return render(request, 'about.html')

def contact(request):
    #return HttpResponse("Hello World you are at contact page")
    return render(request , 'contact.html')