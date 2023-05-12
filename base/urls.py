from django.urls import path
from . import views

urlpatterns = [

    path("", views.homepage, name = "homepage"),

    #login and logout
    #path("login/", views.login_user, name = "login"),

    path("logout/", views.logout_user, name = "logout"),

    #register user
    path("register/", views.register_user, name="register")
    
]