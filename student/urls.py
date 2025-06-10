from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list, name='student-list'),
    path('online-application/', views.online_application, name='online-application'),
]

