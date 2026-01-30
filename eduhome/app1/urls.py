from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.index),
    path('userlogin/', views.userlogin),
    path('signup/', views.signup),
    path('about/', views.about),
    path('course/', views.course),
    path('course-details/', views.course_details),
    path('event/', views.event),
    path('event-details/', views.event_details),
    path('teacher/', views.teacher),
    path('teacher-details/', views.teacher_details),
    path('blog/', views.blog),
    path('blog-details/', views.blog_details),
    path('contact/', views.contact),   
]