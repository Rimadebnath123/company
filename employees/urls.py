from .views import EmployeeViewSet
from .views import RegisterView,LoginView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
     path('employees/', EmployeeViewSet.as_view()),
     path('employees/<int:id>', EmployeeViewSet.as_view()),
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('auth/register/', RegisterView.as_view(),name="auth_register"),
     path('auth/login/', LoginView.as_view(),name="auth_login"),
]
