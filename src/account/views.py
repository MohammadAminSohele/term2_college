from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from rest_framework.throttling import ScopedRateThrottle
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import (
    UserLoginSerializer,
    UserRegisterSerializer,
)

# Create your views here.


class UserLogin(APIView):
    """
    post:
        login a user instance.

        parameters: [username, password]
    """
    
    throttle_scope = "authentication"
    throttle_classes = [
        ScopedRateThrottle,
    ]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():

            user = get_user_model().objects.filter(username=serializer.data.get("username"))
            if not user.exists():
                return Response(
                    {
                        "error!": "User not found",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
            
            refresh = RefreshToken.for_user(user[0])

            context = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return Response(
                data=context,
                status=status.HTTP_200_OK,
            )
    
        else:
            return Response(
                {
                    "error!": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserRegister(APIView):
    """
    post:
        Creates a new user instance.

        parameters: [username, password, confirm_password, email]
    """

    throttle_scope = "authentication"
    throttle_classes = [
        ScopedRateThrottle,
    ]
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():

            try:
                _: None = validate_password(serializer.data.get("password"))
            except ValidationError as err:
                return Response(
                    {"error!": err},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            
            user_exists = get_user_model().objects.filter(username=serializer.data.get("username"))
            if user_exists.exists():
                return Response(
                    {
                        "error!": "User is Exists",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
            get_user_model().objects.create(
                username=serializer.data.get("username"),
                password=serializer.data.get("password"),
                email=serializer.data.get("email"),
            )
            
            return Response(
                {
                    "Success": "the User is created",
                },
                status=status.HTTP_201_CREATED,
            )
        
        else:
            return Response(
                {
                    "error!": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )