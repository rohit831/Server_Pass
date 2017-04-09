from django.shortcuts import render
from rest_framework.response import Response
from .serializers import SareesCategorySerializer
from .models import Sarees
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class SareesCategory(APIView):

        def get(self,request):
            sareesCategory = Sarees.objects.values('category').distinct()
            seriaizer = SareesCategorySerializer( sareesCategory , many= True)
            return Response(seriaizer.data)

