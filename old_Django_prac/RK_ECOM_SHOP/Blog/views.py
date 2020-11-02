from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Blog_View(request):
	return HttpResponse("Welcome To Rk Blog")