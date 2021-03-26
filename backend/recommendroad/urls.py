from django.urls import path
from django.conf import settings
from .views import RecommendTravle
#from .views import *

urlpatterns = [
    path("recommend-travle", RecommendTravle.as_view({"post": "user_option"})),
]