from django.contrib import admin
from django.urls import path


from adminapp import views as admin_views


urlpatterns = [



    path("dashboard/", admin_views.user_dashboard,name="user_dashboard"),

    

]