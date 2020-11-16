from django.http import request
from django.shortcuts import render
from django.http import HttpResponse


def landingView(request):
    return render(request, "landing.html")