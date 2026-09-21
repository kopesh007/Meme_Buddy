from django.urls import path
from .import views

app_name="instagram"

urlpatterns=[
    path("",views.index,name="index"),
    path("new_post/",views.new_post,name="new post"),
    path("detail/<str:slu>",views.detail,name="detail"),
    path("about/",views.about,name="about"),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("dash/",views.dash,name="dash"),
    path("logout/",views.logout,name="logout"),
    path("modify/<int:id>",views.modify,name="modify"),
]