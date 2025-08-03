from django.shortcuts import render

# Create your views here.
def all_hello(request):
    return render(request , 'hello/all_hello.html')
