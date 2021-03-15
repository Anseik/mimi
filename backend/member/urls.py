from django.urls import path
from django.conf import settings
from .views import MemberViewSet

urlpatterns = [
    path("v1", MemberViewSet.as_view({"get": "list", "post": "add"}), name="members"),
    
]