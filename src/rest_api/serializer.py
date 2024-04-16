from rest_framework import serializers 

from .import models


class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'


class StudentTermSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField(method_name='get_student')
    course = serializers.SerializerMethodField(method_name='get_course')
    term = serializers.SerializerMethodField(method_name='get_term')

    def get_student(self, obj):
        return {
            "first_name": obj.student.first_name,
            "last_name": obj.student.last_name,
        }

    def get_course(self, obj):
        return {
            "name": obj.course.name,
            "teacher": obj.course.teacher.last_name,
            "level": obj.course.level.name,
        }
    
    def get_term(self, obj):
        return {
            "name": obj.term.name,
            "startDate": obj.term.startDate,
        }

    class Meta:
        model = models.StudentTerm
        fields = "__all__"


class Teacher_serializer(serializers.ModelSerializer):
    field = serializers.SerializerMethodField(method_name='get_field')

    def get_field(self, obj):
        return {
            "first_name": obj.field.name,
            "last_name": obj.field.study,
        }

    class Meta:
        model = models.Teacher
        fields = '__all__'
