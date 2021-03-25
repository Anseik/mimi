from rest_framework import serializers

class UserOptionSerializer(serializers.Serializer):
    user_date = serializers.DateField()
    user_location = serializers.CharField()
    user_thema = serializers.CharField()
