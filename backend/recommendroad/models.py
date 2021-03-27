
from django.db import models
from member.models import Member




# Create your models here.
#r v s

#store 
class Store(models.Model):
    
    sid = models.CharField(max_length=30, primary_key=True)
    store_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=100, null=True)
    tel = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=100, null=True)
    logitude = models.CharField(max_length=100, null=True)
    review_cnt = models.IntegerField(default=0)
    category = models.CharField(max_length=100, null=True)


    class Meta:
        db_table = "stores"

#menu`  6asd
class Menu(models.Model):
    
    mid = models.CharField(max_length=30, primary_key=True)
    sid = models.ForeignKey(Store, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)
    
    class Meta:
        db_table = "menus"

#review 
class Review(models.Model):
    
    rid = models.CharField(max_length=30, primary_key=True)
    sid = models.ForeignKey(Store, on_delete=models.CASCADE)
    num = models.ForeignKey(Member, on_delete=models.CASCADE)
    total_score = models.CharField(max_length=100, null=True)
    content = models.TextField()
    reg_time = models.TextField()


    class Meta:
        db_table = "reviews"

#landmark 관광지정보 
class Landmark(models.Model):
    
    lid = models.CharField(max_length=30, primary_key=True)
    landmark_name = models.CharField(max_length=200)
    addr = models.CharField(max_length=200, null=True)
    latitude = models.CharField(max_length=200, null=True)
    logitude = models.CharField(max_length=200, null=True)
    facility = models.CharField(max_length=200, null=True)                    #편의시설정보 varchar(200)
    park = models.CharField(max_length=200, null=True)                        #주차가능대수 varchar(200)
    desc = models.TextField()                                      #관광지 소개 text
    tel = models.CharField(max_length=200, null=True)
    theme = models.CharField(max_length=200, null=True)

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
    sidB = models.ForeignKey(Store, on_delete=models.CASCADE,related_name='sidB', null=True)                        #아침코스(식당)  ( stores.sid )
    isSavedB = models.CharField(max_length=100, null=True)                     #아침저장여부                 
    sidL = models.ForeignKey(Store, on_delete=models.CASCADE,related_name='sidL', null=True)                       #점심코스(식당)  ( stores.sid )
    isSavedL = models.CharField(max_length=100, null=True)                     #점심저장여부                 
    sidD = models.ForeignKey(Store, on_delete=models.CASCADE,related_name='sidD', null=True)                        #저녁코스(식당)  ( stores.sid )
    isSavedD = models.CharField(max_length=100, null=True)                     #저녁저장여부                 

    class Meta:
        db_table = "zzimStoreCourses"

#관광지코스
class ZzimLandCourse(models.Model):
    
    num = models.ForeignKey(Member, on_delete=models.CASCADE)  #사용자구분번호 ( members.num )
    lid1 = models.ForeignKey(Landmark, on_delete=models.CASCADE,related_name='lid1', null=True)                #1코스
    lid2 = models.ForeignKey(Landmark, on_delete=models.CASCADE,related_name='lid2', null=True)                #2코스
    lid3 = models.ForeignKey(Landmark, on_delete=models.CASCADE,related_name='lid3', null=True)                #3코스
    lid4 = models.ForeignKey(Landmark, on_delete=models.CASCADE,related_name='lid4', null=True)                #4코스
    isSaved = models.CharField(max_length=100, null=True)                     #코스저장여부
    savedDate = models.CharField(max_length=200, null=True)                   #코스 저장일자                   

    class Meta:
        db_table = "zzimLandCourses"