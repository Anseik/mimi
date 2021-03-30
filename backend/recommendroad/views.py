from django.shortcuts import render
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.views import View
from django.http import Http404, HttpResponse, JsonResponse
from .models import Landmark, ZzimStoreCourse, ZzimLandCourse, Store, Menu
from member.models import Member
from .serializers import UserOptionSerializer, SaveOptionSerializer
from django.core import serializers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from haversine import haversine
from datetime import datetime
from django.utils.dateformat import DateFormat
import urllib.request
import json
import bcrypt
import jwt
import requests
import random
class UserInfo(viewsets.GenericViewSet, View):
    # 저장 정보 전달(아침점심저녁 간단정보)
    def get_user_schedule(self, request, id=''):
        if Member.objects.filter(id = id).exists() :
            #예약 음식 가져오기
            zzimlist = ZzimStoreCourse.objects.filter(id=id)


        return JsonResponse({"message" : "err"}, status=400)
    #저장정보 전달(디테일)
    def get_user_schedule_detail(self, request, id='', date=''):
        if Member.objects.filter(id=id).exists():
            print("z")
        return JsonResponse({"message" : "err"}, status=400)

    # 음식점 정보 전달
    def get_store(self, request, sid='') :
        
        if Store.objects.filter(sid = sid).exists():
            
            result_set = []
            #음식점 정보 가져오기
            store = Store.objects.get(sid=sid)
            
            store_set = { "sid" : store.sid,
                            "store_name" : store.store_name,
                            "branch" : store.branch,
                            "area" : store.area,
                            "tel" : store.tel,
                            "address" : store.address,
                            "latitude" : store.latitude,
                            "logitude" : store.logitude,
                            "review_cnt" : store.review_cnt,
                            "category" : store.category
                            }
            result_set.append(store_set)
            #메뉴 정보 가져오기
            
            if Menu.objects.filter(sid=sid).exists():
                
                menus = Menu.objects.filter(sid=sid)
                menu_info = []
                
                for row in menus.values_list() :
                    
                    add_set = { "mid" : row[0],
                            "sid" : row[1],
                            "menu_name" : row[2],
                            "price" : row[3]
                            }
                    menu_info.append(add_set)
                result_set.append(menu_info)
                return JsonResponse({"message" : result_set}, status=200)
            #메뉴 정보가 없으면
            else :
                
                menu_info = {"mid" : "non"}
                result_set.append(menu_info)
                return JsonResponse({"message" : result_set}, status=200)
            
            
        return JsonResponse({"message" : "err"}, status=400)






class RecommendTravle(viewsets.GenericViewSet, View):
    


    # ZzimLandCourse : 여행 경로 저장
    # ZzimStoreCourse : 여행날짜 음식 저장
    """
        사용자 선호 여행경로 및 식당 저장
        ---
        # 내용
            - id : 사용자 id
            - lid1 : 코스1
            - lid2 : 코스2
            - lid3 : 코스3
            - lid4 : 코스4
            - savedDate : ?
            - sidB : 아침
            - sidL : 점심
            - sidD : 저녁
    """
    @swagger_auto_schema(request_body = SaveOptionSerializer)
    def save_option(self, request) :
        data = json.loads(request.body)
        
        if Member.objects.filter(id = data["id"]).exists():
            print("문제")
            user = Member.objects.get(id=data["id"])
            print(Member.objects.get(id=data["id"]).num)
            print(data["lid1"])
            print(data["lid2"])
            print(data["lid3"])
            print(data["lid4"])
            ZzimLandCourse.objects.create(
                num = str(user.num),
                #유효성 검사해야함
                lid1 = data["lid1"],
                lid2 = data["lid2"],
                lid3 = data["lid3"],
                lid4 = data["lid4"],
                saveDate = DateFormat(datetime.now()).format('Ymd')

            ).save()
            #각 데이터가 있는지 확인해야함
            ZzimStoreCourse.objects.create(
                num = int(user.num),
                sidB = data["sidB"],
                isSavedB = "False",
                sidL = data["sidL"],
                isSavedL = "False",
                sidD = data["sidD"],
                isSavedD = "False"
            ).save()
            return HttpResponse(status=200)
        return JsonResponse({"message" : "Error"}, status=400)

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
        if data["user_location"] == "0" : #서울
            query_set = list(Landmark.objects.filter(addr__contains="서울"))
            print(len(query_set))
            print(str(query_set[0]))
        elif data["user_location"] == 1 : #부산
            query_set = list(Landmark.objects.filter(addr__contains="부산"))
            print(query_set)
        elif data["user_location"] == 2 : #인천
            query_set = list(Landmark.objects.filter(addr__contains="인천"))
            print(query_set)
        elif data["user_location"] == 3 : #대구
            query_set = list(Landmark.objects.filter(addr__contains="대구"))
            print(query_set)
        elif data["user_location"] == 4 : #대전
            query_set = list(Landmark.objects.filter(addr__contains="대전"))
            print(query_set)
        elif data["user_location"] == 5 : #광주
            query_set = list(Landmark.objects.filter(addr__contains="광주"))
            print(query_set)
        elif data["user_location"] == 6 : #울산
            query_set = list(Landmark.objects.filter(addr__contains="울산"))
            print(query_set)
        elif data["user_location"] == 7 : #제주
            query_set = list(Landmark.objects.filter(addr__contains="제주"))
            print(query_set)
        elif data["user_location"] == 8 : #경기
            query_set = list(Landmark.objects.filter(addr__contains="경기"))
            print(query_set)
        elif data["user_location"] == 9 : #강원
            query_set = list(Landmark.objects.filter(addr__contains="강원"))
            print(query_set)
        elif data["user_location"] == 10 : #충남, 충청남도
            query_set = list(Landmark.objects.filter(addr__contains="충남") | Landmark.objects.filter(addr__contains="충청남도"))
            print(query_set)
        elif data["user_location"] == 11 : #충북, 충청북도
            query_set = list(Landmark.objects.filter(addr__contains="충북") | Landmark.objects.filter(addr__contains="충청북도"))
            print(query_set)
        elif data["user_location"] == 12 : #경남, 경상남도
            query_set = list(Landmark.objects.filter(addr__contains="경남") | Landmark.objects.filter(addr__contains="경상남도"))
            print(query_set)
        elif data["user_location"] == 13 : #경북, 경상북도
            query_set = list(Landmark.objects.filter(addr__contains="경북") | Landmark.objects.filter(addr__contains="경상북도"))
            print(query_set)
        elif data["user_location"] == 14 : #전북, 전라북도
            query_set = list(Landmark.objects.filter(addr__contains="전북") | Landmark.objects.filter(addr__contains="전라북도"))
            print(query_set)
        elif data["user_location"] == 15 : #전남, 전라남도
            query_set = Landmark.objects.filter(addr__contains="전남") | Landmark.objects.filter(addr__contains="전라남도")
            if len(query_set) > 0 : #값이 존재
                #랜덤수 생성
                slt = random.randint(0,len(query_set)-1)
                #대입
                select = query_set[slt]
                #수정
                add_set = { "lid" : select.lid,
                            "landmark_name" : select.landmark_name,
                            "addr" : select.addr,
                            "latitude" : select.latitude,
                            "longitude" : select.logitude,
                            "facility" : select.facility,
                            "park" : select.park,
                            "desc" : select.desc,
                            "tel" : select.tel,
                            "theme" : select.theme
                            }
                #위도 경도기준으로 가까운거 3개 뽑기
                #for row in query_set.values_list():

            else : #값이 존재하지 않음 다른거 1개 골라서 추천해야 함
                print("랜덤수: ")
            result_set = []
            for row in query_set.values_list():
                add_set = { "lid" : row[0],
                            "landmark_name" : row[1],
                            "addr" : row[2],
                            "latitude" : row[3],
                            "longitude" : row[4],
                            "facility" : row[5],
                            "park" : row[6],
                            "desc" : row[7],
                            "tel" : row[8],
                            "theme" : row[9]
                            }
                # print(add_set)
                result_set.append(add_set)
            #result_set = serializers.serialize("json", query_set)
            total_result_set = short_path(result_set)
            #여행 테마 기준으로 여행지 1곳 선정
            
            #다른 여행지 추가

            #여행지 거리별 최적화

            # data = {
            # 	"startX" : "126.9850380932383",
            # 	"startY" : "37.566567545861645",
            # 	"endX" : "127.10331814639885",
            # 	"endY" : "37.403049076341794",
            # 	"reqCoordType" : "WGS84GEO",
            # 	"resCchOption" : "0",
            # 	"trafficInfo" : "N"
            # }
            # data = json.dumps(data)
            
            # headers = {'Content-Type': 'application/json', 'appKey': 'l7xxed8f27d952c0448fbf4b9e4d354f551f'}
            # url = "https://apis.openapi.sk.com/tmap/routes?version=1&format=json&callback=result"
            # res = requests.post(url, data=data, headers=headers)
            # json_object = res.json()
            # totalDistance = json_object["features"][0]["properties"]["totalDistance"]
            # print(totalDistance)
            
            
            # json_object = json.loads(res)
            # print("응답")
            # print(json_object)
            return JsonResponse({"recommend" : total_result_set,"recommend_other" : result_set},status=200)
# class OptimizationRoad(view):
#     def 
def short_path(result_set):
    for row in result_set :
        print(row["lid"])
# Create your views here.
