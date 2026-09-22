from django.shortcuts import render,redirect,get_object_or_404
from .models import Posts,cat
from .forms import check_post,login_form
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import regi
from django.contrib.auth import authenticate,login as lin , logout as lout




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
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request,"Post has been uploaded !")
            return redirect("instagram:index")
            print("Dome Mameyyyyyy")

        else:
            messages.error(request,"Something went Wrong !!!")
            print("Wronggggggggggg")
    category = cat.objects.all()
    return render(request,"new_post.html",{'form':form,"categories":category})

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
            messages.success(request,"User Has Been Registered ! , Now You can Login")
            return redirect("instagram:login")
        else:
            print("Wrongggggg")
            return render(request,"register.html",{'form':form,'name':name,'email':email,'password':password,'c_password':c_password})
    return render(request,"register.html",{'form':form})

def login(request):
    form = login_form()
    if request.method == "POST":
        form = login_form(request.POST)
        name = request.POST["name"]
        password = request.POST["password"]
        if form.is_valid():
            user = authenticate(username=name,password=password)
            if user is not None:
                lin(request,user)
                messages.success(request,"You are loggined !")
                return redirect("instagram:index")
        else:
            print("No Done !!!")
            messages.success(request,"Something wents Wrong !")
            return render(request,"login.html",{'form':form,'name':name,'password':password})

    return render(request,"login.html")

def dash(request):
    posts = Posts.objects.filter(user=request.user).order_by("cato")

    return render(request,"dash.html",{'posts':posts})

def logout(request):
    lout(request)
    return redirect("instagram:index")

def modify(request,id):
    post = get_object_or_404(Posts,id=id)
    form = check_post()
    categories = cat.objects.all()
    
    if request.method == 'POST':
        form = check_post(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,"Post has been updated !")
            return redirect("instagram:dash")
        else:
            messages.success(request,"Something Wents Wrong !!!")
        return redirect("instagram:dash")
    return render(request,"edit.html",{'form':form,'post':post,'categories':categories})

def dele(request,id):
    
    post = get_object_or_404(Posts,id=id)
    post.delete()
    messages.success(request,"Post Has Been Deleted !")
    return redirect("instagram:dash")    





# Create your views here.
