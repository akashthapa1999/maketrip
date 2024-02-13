from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render (request, "Home.html")

def Blog(request):
    return render (request, "Blog.html")

def Destination(request):
    return render (request, "Destination.html")

def Packages(request):
    return render (request, "Packages.html")

def About(request):
    return render (request, "About.html")








def Footer(request):
    return render (request, "Footer.html")