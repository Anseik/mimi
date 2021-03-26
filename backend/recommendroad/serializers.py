from .models import Member, Store, Review, Menu, Landmark, ZzimStores, ZzimStoreCourse, ZzimLandCourse
from rest_framework import serializers

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            "sid",
            "store_name",
            "branch",
            "area",
            "tel",
            "address",
            "latitude",
            "longitude",
            "reviewCnt",
            "category_list",
            "image",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            "rid",  
            "sid",  
            "num",  
            "score", 
            "content",  
            "reg_time", 
        )


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "mid",  
            "store",  
            "menu_name",  
            "price"  
        ]

class LandmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landmark
        fields = [
            "lid",  
            "landmark_name",  
            "addr",  
            "latitude",
            "longitude",
            "facility",
            "parking",
            "desc",
            "tel",
            "theme"  
        ]

class ZzimStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZzimStore
        fields = [
            "num",  
            "sid" 
        ]

class ZzimStoreCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZzimStoreCourse
        fields = [
            "num",  
            "sidB",
            "isVisitedB",
            "sidL",
            "isVisitedL",
            "sidD",
            "isVisitedD", 
        ]   

class ZzimLandCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZzimLandCourse
        fields = [
            "num",
            "lid1",
            "lid2",
            "lid3",
            "lid4",
            "isSaved",
            "savedDate"
        ]

class UserOptionSerializer(serializers.Serializer):
    user_date = serializers.DateField()
    user_location = serializers.CharField()
    user_thema = serializers.CharField()
