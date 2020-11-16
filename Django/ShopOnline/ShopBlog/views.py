from django.shortcuts import render
from django.http import request



# Create your views here.
def bloghomeView(request):
	return render(request,'blog/home.html')