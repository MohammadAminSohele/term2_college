from django.urls import path

from .import views

urlpatterns = [
    # student
    path('students/show',views.show_students_info.as_view()),
    path('student/show/<int:pk>',views.show_student_info.as_view()),
    path('student/edit/<int:student_id>',views.edit_student_info.as_view()),
    path('student/register',views.register_student.as_view()),
    path('student/delete/<pk>',views.delete_student.as_view()),
    path('student/register/term',views.register_student_term.as_view()),
    path('student/show/term/<int:term_id>',views.show_studentTerm_info.as_view()),
    path('student/delete/term/<pk>',views.delete_StudentTerm.as_view()),
    path('student/reportcard/<int:term_id>',views.StudentReportCard.as_view()),
    # teacher
    path('teachers/show',views.show_teachers_info.as_view()),
    path('teacher/register',views.register_teacher.as_view()),
    path('teacher/edit/<int:pk>',views.edit_teacher_info.as_view()),
    path('teacher/delete/<pk>',views.delete_teacher_info.as_view()),
    path('teachers/degreeOfeducations',views.TeachersDegreeOfEducations.as_view()),

]
