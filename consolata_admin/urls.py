from django.urls import path
from . import views

app_name = 'consolata_admin'

urlpatterns = [
    path('admin-panel/', views.view_admin_panel, name='admin-panel'),
    path('student-panel/<int:id>', views.view_individual_sudent, name='student-panel'),
    path('update-student/<int:id>', views.update_student_records, name='update-student'),
    path('admit-student/', views.admit_new_student, name='admit-student'),
    path('mailing-list/', views.get_mailing_list, name='mailing-list'), 
    path('send-bulk-email/', views.send_bulk_email, name='send-bulk-email'), 
    path('applications', views.applications, name='applications'),
]

