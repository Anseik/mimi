from django.shortcuts import render
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.views import View
from django.http import Http404, HttpResponse, JsonResponse
# from .models import Member
from .serializers import UserOptionSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import urllib.request
import json
import bcrypt
import jwt
import requests

class RecommendTravle(viewsets.GenericViewSet, View):
    #유저가 선택한 날짜, 지역, 테마
    """
        사용자 선호 여행경로 추천
        ---
        # 내용
            - user_date : 여행날짜
            - user_location : 여행지역
            - user_thema : 여행테마
    """
    @swagger_auto_schema(request_body=UserOptionSerializer)
    def user_option(self, request):
        
        data = json.loads(request.body)
        #user_date
        #user_location
        #user_thema
        #여행 지역 기준으로 조회

        #여행 테마 기준으로 여행지 1곳 선정

        #다른 여행지 추가

        #여행지 거리별 최적화
        data = {
			"startX" : "126.9850380932383",
			"startY" : "37.566567545861645",
			"endX" : "127.10331814639885",
			"endY" : "37.403049076341794",
			"reqCoordType" : "WGS84GEO",
			"resCchOption" : "0",
			"trafficInfo" : "N"
        }
        data = json.dumps(data)
        
        headers = {'Content-Type': 'application/json', 'appKey': 'l7xxed8f27d952c0448fbf4b9e4d354f551f'}
        url = "https://apis.openapi.sk.com/tmap/routes?version=1&format=json&callback=result"
        res = requests.post(url, data=data, headers=headers)
        json_object = res.json()
        totalDistance = json_object["features"][0]["properties"]["totalDistance"]
        print(totalDistance)
        
        print(res.Response)
        # json_object = json.loads(res)
        # print("응답")
        # print(json_object)

# class OptimizationRoad(view):
#     def 

# Create your views here.
