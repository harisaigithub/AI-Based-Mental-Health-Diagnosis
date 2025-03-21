from django.contrib import admin
from django.urls import path


from adminapp import views as admin_views


urlpatterns = [



    path("dashboard/", admin_views.admin_dashboard,name="admin_dashboard"),

    path("logout/", admin_views.admin_logout, name="admin_logout"),
    path("chat/with/bot/", admin_views.user_chatbot, name="user_chatbot"),
    path('new_chat/', admin_views.new_chat, name='new_chat'),
    path("detection/", admin_views.detection, name="detection"),
    path("result/", admin_views.result, name="result"),
    path('feedback', admin_views.Feedback, name = 'feedback'),
    path("profile/", admin_views.user_profile,name="user_profile"),
    path('predictresult', admin_views.predict, name = 'predictresult'),
    path('select_therapy/', admin_views.select_therapy, name='select_therapy'),
    path('download_report/', admin_views.download_report, name='download_report'),
    path('download_specific_report/<int:prediction_id>/', admin_views.download_specific_report, name='download_specific_report'),
    path('mood/assistance/', admin_views.mood_assistance, name='mood_assistance'),
    path('mood/response/<str:mood>/', admin_views.mood_response, name='mood_response'),
    path('yoga/poster/', admin_views.yoga_poster, name='yoga'),



    

]