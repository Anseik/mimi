from django.shortcuts import render
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.views import View
from django.http import Http404, HttpResponse, JsonResponse
from .models import Member
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import json
import bcrypt
import jwt

# class RecommendTravle(viewsets.ModelViewSet, View):
#     #유저가 선택한 날짜, 지역, 테마
#     def user_option(self, request, user_data, user_location, user_thema)



# class OptimizationRoad(view):
#     def 

# Create your views here.
