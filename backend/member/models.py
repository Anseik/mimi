from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.CharField(max_length=10, null=False, primary_key=True)
    password = models.CharField(max_length=50, null=False)
    gender = models.BooleanField(null=False)
    birthday = models.DateField(null=False)
    