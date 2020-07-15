from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurants
from .serializers import Resserializer

class restaurant_list_which_comes_from_database(APIView):
    def get(self,request):
        res = Restaurants.objects.all()
        ser = Resserializer(res,many=True)
        return Response(ser.data)
    def post(self):
        pass