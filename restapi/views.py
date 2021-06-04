import re
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from restapi.serializers import UserSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import WorkshopAccount
# Create your views here.


class RegisterView(APIView):
    permission_classes = (AllowAny,)
    def post(self,req):
        serializer = UserSerializer(data=req.data)
        if serializer.is_valid():
            user = serializer.save()
            user.first_name = req.data.get('name')
            user.save()
            token = Token.objects.create(user = user)
            return Response({'token': token.key})
        return Response(serializer.errors)


class LoginView(APIView):
    permission_classes = (AllowAny,)
    def post(self,req):
        username = req.data.get('username')
        password = req.data.get('password')
        user = authenticate(username = username,password=password)
        content = {}
        if user is not None:
            token,create = Token.objects.get_or_create(user = user)
            content['token'] = token.key
            return Response(content)
        return Response({'err': 'Invalid Credentials'})



class HomeView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,req):
        user = Token.objects.get(key = req.META.get('HTTP_AUTHORIZATION')[6:]).user
        content = {}     
        content['username'] = user.username
        content['name'] = user.first_name
        return Response(content)
        

def addMockData(req):
    import random
    from bs4 import BeautifulSoup
    import requests
    import json
    s = 0
    lst = []
    while(s < 3):
        url = f"https://www.quickerala.com/listings?page={s}&subcategoryId=5395&districtId=3"
        req = requests.get(url)
        soup = BeautifulSoup(req.text,"html.parser")
        data = soup.find_all('button', class_ = "redLink")
    # numbers = soup.find_all('i', title = "Verified number")
  
  
  
        for d in data:
            lst.append(json.loads(d['data-map']))
        s += 1
    
    for item in lst:
        try:
            user = User.objects.create(username = item['name'].replace(" ","").lower())
            user.set_password("password123")
            user.save()
            workshop = WorkshopAccount(
                
                workshopName = item['name'],
                address = item['location'],
                latitude = float(item['latitude']),
                longitude = float(item['longitude']),
                phone = random.randint(7000000000,9999999999)
            )
            workshop.user = user
            workshop.save()
        except :
            print("Repeated Value")
    resp = {
        'len' : len(lst)
    }
    return Response(resp)