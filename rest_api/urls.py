from django.urls import path

from .import views

urlpatterns = [
    path('students/show',views.show_students_info.as_view()),
]
