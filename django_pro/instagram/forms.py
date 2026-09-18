from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class check_post(forms.Form):
    image = forms.ImageField(label="Image",required=True,max_length=500)
    caption = forms.CharField(label="Description",required=True,max_length=500)
    cato = forms.IntegerField(label="Category",required=True)

class regi(forms.ModelForm):
    username = forms.CharField(label="Name",required=True,max_length=100)
    email = forms.EmailField(label="Email",required=True)
    password = forms.CharField(label="Password",required=True,max_length=200)
    c_password = forms.CharField(label="Conform Password",required=True,max_length=200)


    class Meta:
        model = User
        fields = ["username","email","password"]


    def clean(self):

        cl_data = super().clean()
        u_name = cl_data.get("username")
        password = cl_data.get("password")
        c_password = cl_data.get("c_password")
        email = cl_data.get("email")

        if(password and c_password and password != c_password ):
            raise forms.ValidationError("Password mismatch or incorrect !")
        
        if(User.objects.filter(email=email).exists()):
            raise forms.ValidationError("This Email Was Already Registered ! ")
            

class login_form(forms.Form):
    name = forms.CharField(label="User Name",max_length=200,required=True)
    password = forms.CharField(label="Password",max_length=200,required=True)

    def clean(self):
        cl_data = super().clean()
        u_name = cl_data.get("name")
        password = cl_data.get("password")

        user = authenticate(username=u_name,password=password)

        if(user is None):
            raise forms.ValidationError("User Not Found ! , Please Register !")


        






