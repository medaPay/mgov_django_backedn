from django.urls import path
from .views import UserRegistration, DeveloperRegistration, CustomLoginView,send_otp,verify_otp
from . import views

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user_register'),
    path('developer/register/', DeveloperRegistration.as_view(), name='developer_register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("send-otp/", send_otp, name="send_otp"),
    path("verify-otp/", verify_otp, name="verify_otp"),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('verify-reset-otp/', views.VerifyResetOTPView.as_view(), name='verify-reset-otp'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset-password'),
    path('change-developer-password/', views.ChangeDeveloperPasswordView.as_view(), name='change-developer-password'),
]
