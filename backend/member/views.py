from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.views import View
from django.http import Http404, HttpResponse, JsonResponse
from .models import Member
from .serializers import MemberSerializer, EmailAuthSerializer
from backend.settings import SECRET_KEY, EMAIL_HOST_USER
from .token import email_auth_num
from django.core.mail import EmailMessage
import json
import bcrypt
import jwt


#GenericViewSet -> get_queryset, get_object사용

# Create your views here.
#이메일 인증
class email_auth(viewsets.GenericViewSet, View):
    serializer_class = EmailAuthSerializer
    def get(self, request):
        data = json.loads(request.body)
        user_email = data["id"]
        #전처리 한번 필요
        token = email_auth_num()
        message = f"인증번호는 {token} 입니다."
        mail_title = "mimi 이메일 인증 메일입니다."
        email = EmailMessage(mail_title, message, to=[user_email])
        email.send()


#회원가입
class MemberView(viewsets.GenericViewSet, View):
    #Swagger 설명을 위해 필요
    serializer_class = MemberSerializer

    #회원가입
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Member.objects.filter(id = data["id"]).exists():
                return JsonResponse({"message" : "EXISTS_ID"}, status=400)
            #num 값 갱신
            user_email = data["id"]
            #전처리 한번 필요
            
            curr_max_num = Member.objects.all()
            print("확인")
            print(curr_max_num)
            if(curr_max_num==None):
                curr_max_num = 0
            else:
                curr_max_num = 1
            Member.objects.create(
                num = curr_max_num,
                id = data["id"],
                password = bcrypt.hashpw(data["password"].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8"),
                gender = data["gender"],
                birthday = data["birthday"]
            ).save()
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"},status=400)
    #id중복여부 api
    def get(self, request):
        try:
            if Member.objects.filter(id = data["id"]).exists():
                return JsonResponse({"message" : "EXISTS_ID"}, status=400)
            return JsonResponse({"message" : "ALLOW"}, status=200)

        except KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"},status=400)
#로그인 클래스
class SignView(viewsets.GenericViewSet,View):
    serializer_class = MemberSerializer
    def post(self, request):
        data = json.loads(request.body)

        try:
            if Member.objects.filter(id = data["id"]).exists():
                user = Member.objects.get(id = data["id"])
                #로그인 성공
                if bcrypt.checkpw(data['password'].encode("UTF-8"), user.password.encode("UTF-8")):
                    num = str(user.num)
                    
                    token = jwt.encode({"user" : num}, SECRET_KEY, algorithm="HS256")
                    
                    return JsonResponse({"token" : token},status=200)
                #실패
                return HttpResponse(status=401)
            return HttpResponse(status=401)# 400으로 적힘 두개 차이점 알기
        except KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"}, status=400)

class MemberViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, View):
    serializer_class = MemberSerializer
    def get_queryset(self):
        conditions = {
            "id" : self.kwargs.get("Member_num", None),
            "password" : self.request.GET.get("password", None),
            "gender" : self.request.GET.get("gender", None),
            "birthday" : self.request.GET.get("birthday", None)
        }
        conditions = {
            Key : val for key, val in conditions.items() if val is not None
        }
        members = Member.objects.filter(**conditions)
        if not members.exists():
            raise Http404
        return members

        