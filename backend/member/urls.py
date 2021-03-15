from django.urls import path
from django.conf import settings
from .views import MemberViewSet

urlpatterns = [
    path("v1/member", MemberViewSet.as_view({"get": "list", "post": "add"}), name="members"),
    
]