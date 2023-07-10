from django.shortcuts import render

# Create your views here.
name = "Register"

def rigister(request):
    return render(request, "register.html")