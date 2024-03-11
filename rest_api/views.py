from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Student
from .serializer import Student_serializer

# Create your views here.

class show_students_info(APIView):
    def get(self,request:Request):
        students_query=Student.objects.all()
        serializer=Student_serializer(instance=students_query,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
