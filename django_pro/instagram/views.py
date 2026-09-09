from django.shortcuts import render

user = {"username":"KOPESH","caption":"Hi guyssssssssssssssss"}


def index(request):
    return render(request,"index.html",{"user":user})

# Create your views here.
