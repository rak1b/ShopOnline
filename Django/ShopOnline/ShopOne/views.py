from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def navview(request):
    return render(request, 'shop/Nav.html')

def imageview(request):
    return render(request, 'shop/img.html')

def homeview(request):
    return render(request, 'shop/home.html')

def pracview(request):
    return render(request,'shop/prac.html')
