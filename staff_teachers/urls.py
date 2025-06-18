from django.urls import path
from . import views

app_name = 'staff_teachers'

urlpatterns = [
    path('teachers-pay/', views.view_teachers_pay, name='teachers-pay'),
    path('admin-office/', views.admin_office, name='admin-office'),
    path('timetable/', views.create_timetable, name='timetable'),
    path('edit-table/<int:id>', views.edit_time_table, name='edit-table'),
    path('delete-table/<int:id>', views.delete_timetable_raw, name='delete-table'),
    path('fetch-sign/', views.fetch_student_class_sign, name='fetch-sign'),
    path('upload-csv/', views.upload_results_csv, name='upload-csv'),
    path('results/', views.show_exam_results, name='results')
]
