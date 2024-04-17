from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics

from .models import Student, Teacher, StudentTerm
from .serializer import (
    Student_serializer,
    Teacher_serializer,
    StudentTermSerializer,
)


# Create your views here.

class show_students_info(ListAPIView):

    permission_classes = [
        IsAdminUser,
    ]

    serializer_class = Student_serializer
    filterset_fields = [
        "regdate",
    ]
    search_fields = [
        "nat_code",
        "last_name",
        "email",
        "mobile",
    ]
    ordering_fields = (
        "last_name",
        "first_name",
    )

    def get_queryset(self):
        return Student.objects.all()


class show_student_info(APIView):

    permission_classes = [
        IsAdminUser,
    ]

    def get(self, request: Request, student_id: int):
        selected_student = get_object_or_404(Student, pk=student_id)
        serializer = Student_serializer(instance=selected_student)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class show_studentTerm_info(APIView):

    def get(self, request: Request, student_id, term_id):

        selected_term = StudentTerm.objects.filter(
            student_id=student_id, 
            term_id=term_id,
        )

        if selected_term.exists():
            get_serialize = StudentTermSerializer(many=True, instance=selected_term)
            return Response(data=get_serialize.data, status=status.HTTP_200_OK)
        
        return Response(
            {
                "Not Found": "the user not found",
            },
            status=status.HTTP_404_NOT_FOUND,
        )


class edit_student_info(APIView):

    permission_classes = [
        IsAdminUser,
    ]

    def get(self, request: Request, student_id: int):
        selected_student = get_object_or_404(Student, pk=student_id)
        serializer = Student_serializer(instance=selected_student)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, student_id: int):
        selected_student = get_object_or_404(Student, pk=student_id)
        edit = Student_serializer(instance=selected_student, data=request.data)
        if edit.is_valid():
            edit.save()
            return Response(data=edit.data, status=status.HTTP_202_ACCEPTED)
        return Response(
            data={
                "Bad Request": "Please enter again data",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class edit_StudentTerm_info(APIView):

    def get_object(self, student_term: int):
        try:
            selected_term = StudentTerm.objects.get(pk=student_term)
            return selected_term
        except StudentTerm.DoesNotExist:
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request, student_term: int):
        selected_term = self.get_object(student_term)
        get_serialize = StudentTermSerializer(instance=selected_term)
        return Response(data=get_serialize.data, status=status.HTTP_200_OK)

    def put(self, request: Request, student_term: int):
        selected_term = self.get_object(student_term)
        put_serialize = StudentTermSerializer(instance=selected_term, data=request.data)
        if put_serialize.is_valid():
            put_serialize.save()
            return Response(data=put_serialize.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=None, status=status.HTTP_400_BAD_REQUEST)


class delete_student(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_serializer

    def delete(self, request: Request, pk):
        return self.destroy(request)


class delete_StudentTerm(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = StudentTerm.objects.all()
    serializer_class = StudentTermSerializer

    def delete(self, request: Request, pk):
        return self.destroy(request)


class register_student(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_serializer

    def post(self, request: Request):
        return self.create(request)


class register_student_term(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = StudentTerm.objects.all()
    serializer_class = StudentTermSerializer

    def post(self, request: Request):
        return self.create(request)


class show_teachers_info(ListAPIView):

    permission_classes = [
        IsAdminUser,
    ]

    serializer_class = Teacher_serializer
    filterset_fields = [
        "regdate",
    ]
    search_fields = [
        "nat_code",
        "last_name",
        "email",
        "mobile",
    ]
    ordering_fields = (
        "last_name",
        "first_name",
    )

    def get_queryset(self):
        return Teacher.objects.all()


class register_teacher(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Teacher.objects.all()
    serializer_class = Teacher_serializer

    def get(self, request: Request):
        return self.list(request)

    def post(self, request: Request):
        return self.create(request)


class delete_teacher_info(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Teacher.objects.all()
    serializer_class = Teacher_serializer

    def delete(self, request: Request, pk):
        return self.destroy(request)


class edit_teacher_info(APIView):

    permission_classes = [
        IsAdminUser,
    ]

    def get(self, request: Request, teacher_id):
        selected_teacher = get_object_or_404(Teacher, pk=teacher_id)
        get_serialize = Teacher_serializer(instance=selected_teacher)
        return Response(data=get_serialize.data, status=status.HTTP_200_OK)

    def put(self, request: Request, teacher_id):
        selected_teacher = get_object_or_404(Teacher, pk=teacher_id)
        edit_serialize = Teacher_serializer(
            instance=selected_teacher, data=request.data
        )
        if edit_serialize.is_valid():
            edit_serialize.save()
            return Response(data=edit_serialize.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(
            data={
                "Bad Request": "Please enter again data",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
