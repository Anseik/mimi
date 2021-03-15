from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.views import View
from django.http import Http404

from .models import Member
from .serializers import MemberSerializer

# Create your views here.

class MemberViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, View):
    serializer_class = MemberSerializer
    def get_queryset(self):
        conditions = {
            "id" : self.kwargs.get("Member_num", None),
            "password" : self.request.GET.get("password", None),
            "gender" : self.request.GET.get("gender", None),
            "birthday" : self.request.GET.get("birthday", None)
        }
        conditions = {
            Key : val for key, val in conditions.items() if val is not None
        }
        members = Member.objects.filter(**conditions)
        if not members.exists():
            raise Http404
        return members