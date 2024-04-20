from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from . import views

urlpatterns = [
    # account
    path('login/', views.UserLogin.as_view()),
    path('register/', views.UserRegister.as_view()),

    # jwt auth
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
