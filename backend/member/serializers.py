from .models import Member
from rest_framework import serializers

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        member = Member.objects.all()
        model = Member
        fields = '__all__'