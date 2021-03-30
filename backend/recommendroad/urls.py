from django.urls import path
from django.conf import settings
from .views import RecommendTravle, UserInfo
#from .views import *

urlpatterns = [

    path("recommend-travle", RecommendTravle.as_view({"post": "user_option"})),
    path("save-option", RecommendTravle.as_view({"post": "save_option"})),
    path("get-store-info/<str:sid>", UserInfo.as_view({"get": "get_store"})),
    path("get-user-schedule/<str:id>", UserInfo.as_view({"get": "get_user_schedule"})),
    
]
    