from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Shop_View(request):
	return render(request,'Shop/home.html')