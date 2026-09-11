from django.shortcuts import render
from .models import Posts,cat

user = {"username":"KOPESH","caption":"Hi guyssssssssssssssss"}


def index(request):
    posts = Posts.objects.all()
    return render(request,"index.html",{"posts":posts})

# Create your views here.
