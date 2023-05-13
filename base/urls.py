from django.urls import path
from . import views

urlpatterns = [

    path("", views.homepage, name = "homepage"),

    #login and logout
    #path("login/", views.login_user, name = "login"),

    path("logout/", views.logout_user, name = "logout"),

    #register user
    path("register/", views.register_user, name="register"),
    
    #customer record
    path("record/<int:pk>/", views.customer_record ,name = "record"),

    #delete user
    path("delete_record/<int:pk>", views.delete_record, name = "delete_record"),

    #add_record
    path("add_record", views.add_record, name="add_record"),

    #update record
    path("update_record/<int:pk>/", views.update_record, name="update_record"),
]