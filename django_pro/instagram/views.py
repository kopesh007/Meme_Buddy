from django.shortcuts import render,redirect
from .models import Posts,cat
from .forms import check_post,login_form
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import regi

user = {"username":"KOPESH","caption":"Hi guyssssssssssssssss"}


def index(request):
    posts = Posts.objects.all()
    return render(request,"index.html",{"posts":posts})


def new_post(request):
    form = check_post()
    if request.method == "POST":
        cap=request.POST["caption"]
        ima = request.FILES["image"]
        ca = request.POST["cato"]
        form = check_post(request.POST,request.FILES)

        if form.is_valid():
            c = cat.objects.get(id=ca)
            Posts.objects.create(caption=cap,image=ima,cato=c)
            messages.success(request,"Post has been uploaded !")
            print("Dome Mameyyyyyy")

        else:
            messages.error(request,"Something went Wrong !!!")
            print("Wronggggggggggg")
    category = cat.objects.all()
    return render(request,"new_post.html",{"categories":category})

def detail(request,slu):
    try:
        post = Posts.objects.get(sl=slu)
        rel_posts = Posts.objects.filter(cato=post.cato).exclude(id=post.id)
    except Exception:
        post = None
        messages.error(request,"Post hasn't been found")
        return redirect("instagram:index")
    return render(request,"detail.html",{'post':post,'related':rel_posts})

def about(request):
    return render(request,"about.html")

def register(request):
    form = regi()
    if request.method == "POST":
        form = regi(request.POST)
        name = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        c_password = request.POST["c_password"]
        if form.is_valid():
            print("done")
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request,"User Has Been Registered ! ")
            return redirect("instagram:index")
        else:
            print("Wrongggggg")
            return render(request,"register.html",{'form':form,'name':name,'email':email,'password':password,'c_password':c_password})
    return render(request,"register.html",{'form':form})

def login(request):
    form = login_form()
    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            print("done")
        else:
            print("No Done !!!")

    return render(request,"login.html")

# Create your views here.
