from django.contrib import admin
from django.urls import path


from userapp import views as user_views


urlpatterns = [

    path("our-services/",user_views.our_services,name="our_services"),
    path("contact/",user_views.contact,name="contact"),
    path("about/",user_views.about,name="about"),
    path("login/",user_views.login,name="login"),
    path("register/", user_views.user_register,name="user_register"),
    path("otp/",user_views.user_otp,name="user_otp"),
    path("logout/",user_views.user_logout,name="user_logout"),




    path("dashboard/", user_views.user_dashboard,name="user_dashboard"),
    path("chatbot/", user_views.chatbot,name="chatbot"),
    path("profile/", user_views.user_profile,name="user_profile"),
    path('feedback/',user_views.user_feedback,name="user_feedback"),


   

    

]