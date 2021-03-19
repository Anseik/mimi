from django.urls import path
from django.conf import settings
from .views import MemberViewSet, MemberView, SignView, email_auth

urlpatterns = [
<<<<<<< HEAD
    path("v1/member", MemberViewSet.as_view({"get": "list", "post": "add"}), name="members"),
    #회원가입
    path("sign-up", MemberView.as_view({"post": "post"})),
    #로그인
    path("sign-in", SignView.as_view({"post": "post"})),
    #이메일 인증
    path("auth-email", email_auth.as_view({"get": "get"})),
=======
    path("v1", MemberViewSet.as_view({"get": "list", "post": "add"}), name="members"),
    
>>>>>>> c62eeda0ece9a05640431984f4fb3037ac1f8012
]