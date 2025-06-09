from django.urls import path
from . import views

app_name = 'staff_teachers'

urlpatterns = [
    path('teachers-pay/', views.view_teachers_pay, name='teachers-pay'),
    path('admin-office/', views.admin_office, name='admin-office'),
    
]
