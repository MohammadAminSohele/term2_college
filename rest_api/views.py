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