from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics

from .models import Student, Teacher, StudentTerm
from .serializer import (
    StudentSerializer,
    StudentTermSerializer,
    StudentTermRegisterSerializer,
    TeacherSerializer,
    TeacherRegisterEditSerializer,
    TeacherDegreeOfEducationSerializer,
)

from permissions import (
    IsAdminUserOrUser,
    IsSuperUser,
    IsSuperuserOrStudentUser,
)

# Create your views here.

class show_students_info(ListAPIView):
    """
    get:
        Returns all existing students.
    """

    permission_classes = [
        IsAdminUser,
    ]

    serializer_class = StudentSerializer
    filterset_fields = [
        "regdate",
    ]
    search_fields = [
        "nat_code",
        "user__last_name",
        "user__email",
        "mobile",
    ]
    ordering_fields = (
        "user__last_name",
        "user__first_name",
    )

    def get_queryset(self):
        return Student.objects.all()


class show_student_info(RetrieveAPIView):
    """
    get:
        Returns the details of a student instance. Searches student using pk field.
    """

    serializer_class = StudentSerializer
    permission_classes = [
        IsAdminUserOrUser,
    ]
    lookup_field = "pk"

    def get_queryset(self):
        return Student.objects.all()


class edit_student_info(APIView):
    """
    get:
        Returns the details of a student instance. Searches student using pk field.

    put:
        Updates an existing student. Returns updated student data.

        parameters: exclude = [user]
    """

    permission_classes = [
        IsAdminUser,
    ]

    def get(self, request: Request, student_id: int):
        selected_student = get_object_or_404(Student, pk=student_id)
        serializer = StudentSerializer(instance=selected_student)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, student_id: int):
        selected_student = get_object_or_404(Student, pk=student_id)
        edit = StudentSerializer(instance=selected_student, data=request.data)
        if edit.is_valid():
            edit.save()
            return Response(data=edit.data, status=status.HTTP_202_ACCEPTED)
        return Response(
            data={
                "Bad Request": "Please enter again data",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class delete_student(mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    delete:
        Delete an existing student. search student for delete with pk.
    """

    permission_classes = [
        IsSuperUser,
    ]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    def delete(self, request: Request, pk):
        return self.destroy(request)


class register_student(mixins.CreateModelMixin, generics.GenericAPIView):
    """
    post:
        Creates a new student instance.

        parameters: exclude = [user]
    """

    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request: Request):
        return self.create(request)
    
    def perform_create(self, serializer):
        return serializer.save(
            user=self.request.user,
            )


class show_studentTerm_info(APIView):
    """
    get:
        Returns a list of student terms.
    """

    permission_classes = [
        IsAuthenticated,
    ]
    
    def validate_auth(self, request):
        if  request.user.is_superuser or\
            request.user.is_staff:
            return True
        else:
            return Response(
                {
                    "Access denied": "You do not have access to this page",
                },
                status=status.HTTP_403_FORBIDDEN,
            )


    def get(self, request: Request, term_id):
        user = get_object_or_404(Student, user=request.user)
        selected_term = StudentTerm.objects.filter(
            student_id=user.id, 
            term_id=term_id,
        )

        if not selected_term.exists():
            return Response(
                {
                    "Not Found": "the user not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        if self.validate_auth(request):
            if selected_term.exists():
                get_serialize = StudentTermSerializer(many=True, instance=selected_term)
                return Response(data=get_serialize.data, status=status.HTTP_200_OK)
        
            return Response(
                {
                    "Not Found": "the user not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


class StudentReportCard(APIView):
    """
    get:
        Returns student report card in one term.
    """

    permission_classes = [
        IsAuthenticated,
    ]
    
    def get(self, request: Request, term_id: int):
        user = get_object_or_404(Student, user=request.user)
        selected_term = StudentTerm.objects.filter(
            student_id=user.id, 
            term_id=term_id,
        )

        if not selected_term.exists():
            return Response(
                {
                    "error": "The desired term not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        
        context = {
            "first name": request.user.first_name,
            "last name": request.user.last_name,
            "term name": selected_term[0].term.name,
        }
    
        failes, grades, unit_course = {}, {}, {}
        counter, sum, units = 0, 0, 0
        for i in selected_term:
            unit_course[i.course.name] = i.course.unit
            units += i.course.unit
            sum += (i.grade) * i.course.unit; counter += i.course.unit
            grades[i.course.name] = i.grade
            if i.grade < 10:
                failes[i.course.name] = i.grade

        context["grades"] = grades
        context["failes"] = failes
        context["average"] = sum / counter
        context["sum"] = sum
        context["units"] = units
        context["unit course"] = unit_course

        return Response(
            data=context,
            status=status.HTTP_200_OK,
        )


class delete_StudentTerm(mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    delete:
        Delete an existing student term. search student term with pk.
    """

    permission_classes = [
        IsSuperuserOrStudentUser,
    ]
    queryset = StudentTerm.objects.all()
    serializer_class = StudentTermSerializer

    def delete(self, request: Request, pk):
        return self.destroy(request)


class register_student_term(mixins.CreateModelMixin, generics.GenericAPIView):
    """
    post:
        Creates a new student term instance. Returns student term data.

        parameters: exclude = [student]
    """

    permission_classes = [
        IsSuperuserOrStudentUser,
    ]
    queryset = StudentTerm.objects.all()
    serializer_class = StudentTermRegisterSerializer

    def post(self, request: Request):
        return self.create(request)

    def perform_create(self, serializer):
        student = Student.objects.get(user=self.request.user)
        return serializer.save(
            student=student,
            )


class show_teachers_info(ListAPIView):
    """
    get:
        Returns all existing teachers.
    """

    permission_classes = [
        IsAdminUser,
    ]

    serializer_class = TeacherSerializer
    filterset_fields = [
        "regdate",
    ]
    search_fields = [
        "nat_code",
        "user__last_name",
        "user__email",
        "mobile",
    ]
    ordering_fields = (
        "user__last_name",
        "user__first_name",
    )

    def get_queryset(self):
        return Teacher.objects.all()


class register_teacher(mixins.CreateModelMixin, generics.GenericAPIView):
    """
    post:
        Creates a new user instance.

        parameters: exclude = [user]
    """

    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Teacher.objects.all()
    serializer_class = TeacherRegisterEditSerializer

    def post(self, request: Request):
        return self.create(request)

    def perform_create(self, serializer):
        return serializer.save(
            user=self.request.user,
            )


class delete_teacher_info(mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    delete:
        Delete an existing teacher.
    """

    permission_classes = [
        IsSuperUser,
    ]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def delete(self, request: Request, pk):
        return self.destroy(request)


class edit_teacher_info(UpdateAPIView):
    """
    put:
        Updates an existing teacher. Returns updated teacher data.

        parameters: exclude = [user]
    """
    serializer_class = TeacherRegisterEditSerializer
    permission_classes = [
        IsAdminUserOrUser,
    ]
    lookup_field = "pk"

    def get_queryset(self):
        return Teacher.objects.all()


class TeachersDegreeOfEducations(ListAPIView):
    """
    get:
        Returns all Teachers Degree Of Educations.
    """

    serializer_class = TeacherDegreeOfEducationSerializer
    filterset_fields = [
        "field",
    ]
    search_fields = [
        "user__first_name",
        "user__last_name",
    ]

    def get_queryset(self):
        return Teacher.objects.all()