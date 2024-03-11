from django.urls import path

from .import views

urlpatterns = [
    # student
    path('students/show',views.show_students_info.as_view()),
    path('students/show/<int:student_id>',views.show_student_info.as_view()),
    path('students/edit/<int:student_id>',views.edit_student_info.as_view()),
    path('student/register',views.register_student.as_view()),
    # teacher
    path('teachers/show',views.show_teachers_info.as_view()),
    path('teacher/register',views.register_teacher.as_view()),

]
