from django.shortcuts import render

# Create your views here.
name = "Home"

def home(request):
    return render(request, "Home/index.html")
