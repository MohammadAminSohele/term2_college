from rest_framework import serializers 

from .import models


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name='get_user')

    def get_user(self, obj):
        return {
            "username": obj.user.username,
        }
    
    class Meta:
        model = models.Student
        fields = '__all__'


class StudentTermSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField(method_name='get_student')
    course = serializers.SerializerMethodField(method_name='get_course')
    term = serializers.SerializerMethodField(method_name='get_term')

    def get_student(self, obj):
        return {
            "first_name": obj.student.user.first_name,
            "last_name": obj.student.user.last_name,
        }

    def get_course(self, obj):
        return {
            "name": obj.course.name,
            "teacher": obj.course.teacher.user.last_name,
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


class StudentTermRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentTerm
        exclude = [
            "student",
        ]


class TeacherSerializer(serializers.ModelSerializer):
    field = serializers.SerializerMethodField(method_name='get_field')

    def get_field(self, obj):
        return {
            "name": obj.field.name,
            "study": obj.field.study,
        }

    class Meta:
        model = models.Teacher
        fields = '__all__'


class TeacherRegisterEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        exclude = [
            "user",
        ]

class TeacherDegreeOfEducationSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name='get_user')

    def get_user(self, obj):
        return {
            "first name": obj.user.first_name,
            "last name": obj.user.last_name,
        }
    
    field = serializers.SerializerMethodField(method_name='get_field')

    def get_field(self, obj):
        return {
            "name": obj.field.name,
            "study": obj.field.study,
        }

    class Meta:
        model = models.Teacher
        fields = [
            "user", "field",
        ]
