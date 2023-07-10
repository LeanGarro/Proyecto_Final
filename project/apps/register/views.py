from django.shortcuts import render

# Create your views here.
name = "Register"

def register(request):
    return render(request, "register/register.html")



