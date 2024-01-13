from django.urls import path
from django.contrib import admin
from . import views



urlpatterns = [

    path('',views.about,name="about"),
    path('resume.html',views.resume,name="resume"),
    path('calendar.html',views.calen,name="calendar"),
    path('skills.html',views.skills,name="skills"),
    path('contact.html',views.contact,name="contact"),
    path('comments.html',views.comments,name="comments"),
    path('', views.linkedin,name="linkedin"),

]

#