from django.shortcuts import render, redirect

def homepage(request):
    return render(request, "Bugz/homepage.html")

def contact(request):
    return render(request, "Bugz/contact.html")

def about(request):
    return render(request, "Bugz/about.html")

def login(request):
    return render(request, "Bugz/login.html")
