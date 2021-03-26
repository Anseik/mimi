from django.db import models
from ../member/models import member

# Create your models here.
#r v s

#store 
class Store(models.Model):
    
    sid = models.CharField(max_length=30, primary_key=True)
    store_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    latitude = models.CharField(max_length=100)
    logitude = models.CharField(max_length=100)
    category = models.CharField(max_length=100)


    class Meta:
        db_table = "stores"

#menu`  6asd
class Menu(models.Model):
    
    mid = models.CharField(max_length=30, primary_key=True)
    sid = models.ForeignKey(Store, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    
    class Meta:
        db_table = "menus"

#review 
class Review(models.Model):
    
    rid = models.CharField(max_length=30, primary_key=True)
    sid = models.ForeignKey(Store, on_delete=models.CASCADE)
    num = models.ForeignKey(Member, on_delete=models.CASCADE)
    total_score = models.CharField(max_length=100)
    content = models.TextField()
    reg_time = models.TextField()


    class Meta:
        db_table = "reviews"

#landmark 관광지정보 
class Landmark(models.Model):
    
    lid = models.CharField(max_length=30, primary_key=True)
    landmark_name = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    logitude = models.CharField(max_length=200)
    facility = models.CharField(max_length=200)                    #편의시설정보 varchar(200)
    park = models.CharField(max_length=200)                        #주차가능대수 varchar(200)
    desc = models.TextField()                                      #관광지 소개 text
    tel = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)

    class Meta:
        db_table = "landmarks"

#맛집코스
class ZzimStore(models.Model):
    
    num = models.ForeignKey(Member, on_delete=models.CASCADE)  #사용자구분번호 ( members.num )
    sid = models.ForeignKey(Store, on_delete=models.CASCADE)                        #아침코스(식당)  ( stores.sid )           

    class Meta:
        db_table = "zzimStores"

#맛집코스
class ZzimStoreCourse(models.Model):
    
    num = models.ForeignKey(Member, on_delete=models.CASCADE)  #사용자구분번호 ( members.num )
    sidB = models.ForeignKey(Store, on_delete=models.CASCADE)                        #아침코스(식당)  ( stores.sid )
    isSavedB = models.CharField(max_length=100)                     #아침저장여부                 
    sidL = models.ForeignKey(Store, on_delete=models.CASCADE)                       #점심코스(식당)  ( stores.sid )
    isSavedL = models.CharField(max_length=100)                     #점심저장여부                 
    sidD = models.ForeignKey(Store, on_delete=models.CASCADE)                        #저녁코스(식당)  ( stores.sid )
    isSavedD = models.CharField(max_length=100)                     #저녁저장여부                 

    class Meta:
        db_table = "zzimStoreCourses"

#관광지코스
class ZzimLandCourse(models.Model):
    
    num = models.ForeignKey(Member, on_delete=models.CASCADE)  #사용자구분번호 ( members.num )
    lid1 = models.ForeignKey(Landmark, on_delete=models.CASCADE)                #1코스
    lid2 = models.ForeignKey(Landmark, on_delete=models.CASCADE)                #2코스
    lid3 = models.ForeignKey(Landmark, on_delete=models.CASCADE)                #3코스
    lid4 = models.ForeignKey(Landmark, on_delete=models.CASCADE)                #4코스
    isSaved = models.CharField(max_length=100)                     #코스저장여부
    savedDate = models.CharField(max_length=200)                   #코스 저장일자                   

    class Meta:
        db_table = "zzimLandCourses"