from rest_framework import serializers 

from .import models

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.Student
        fields='__all__'

class Teacher_serializer(serializers.ModelSerializer):
    class Meta:
        model=models.Teacher
        fields='__all__'