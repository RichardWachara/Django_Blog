# from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse("<h2>Home Page</h2>")

def home(request):
    return render(request,"index.html")