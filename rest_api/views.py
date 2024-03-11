from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins,generics

from .models import Student,Teacher
from .serializer import Student_serializer,Teacher_serializer

# Create your views here.

class show_students_info(APIView):
    def get(self,request:Request):
        students_query=Student.objects.all()
        serializer=Student_serializer(instance=students_query,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
class show_student_info(APIView):
    def get_object(self,student_id:int):
        try:
            selected_student=Student.objects.get(pk=student_id)
            return selected_student
        except Student.DoesNotExist:
            return Response(data=None,status=status.HTTP_404_NOT_FOUND)
    def get(self, request:Request,student_id:int):
        selected_student=self.get_object(student_id)
        serializer=Student_serializer(instance=selected_student)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
class edit_student_info(APIView):
    def get_object(self,student_id:int):
        try:
            selected_student=Student.objects.get(pk=student_id)
            return selected_student
        except Student.DoesNotExist:
            return Response(data=None,status=status.HTTP_404_NOT_FOUND)
    def get(self, request:Request,student_id:int):
        selected_student=self.get_object(student_id)
        serializer=Student_serializer(instance=selected_student)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def put(self, request:Request,student_id:int):
        selected_student=self.get_object(student_id)
        edit=Student_serializer(instance=selected_student,data=request.data)
        if edit.is_valid():
            edit.save()
            return Response(data=edit.data,status=status.HTTP_202_ACCEPTED)
        return Response(data=None,status=status.HTTP_400_BAD_REQUEST)

class register_student(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=Student_serializer

    def post(self,request:Request):
        return self.create(request)
    
class show_teachers_info(APIView):
    def get(self,request:Request):
        teachers_query=Teacher.objects.all()
        serializer=Teacher_serializer(instance=teachers_query,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
class register_teacher(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Teacher.objects.all()
    serializer_class=Teacher_serializer

    def post(self,request:Request):
        return self.create(request)