from django.db import models

# Create your models here.
class Member(models.Model):
    #num변수 선언해야함
    
    id = models.EmailField(max_length=50, null=False, primary_key=True) #email형식
    num = models.IntegerField(unique=True)
    password = models.CharField(max_length=200, null=False)
    gender = models.BooleanField(null=False)
    birthday = models.DateField(null=False)
    

    class Meta:
        db_table = "members"
    