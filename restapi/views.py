from django.contrib.auth import authenticate
from .models import WorkshopAccount
from rest_framework import serializers
from restapi.serializers import SearchSerializer, UserSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import WorkshopAccount
from django.db.models import Q
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
        

class SearchView(APIView):
    permission_classes = (AllowAny,)
    def get(self,req):
        query = req.GET.get('query')
        queryset = WorkshopAccount.objects.filter(Q(address__contains = query) | Q(workshopName__contains = query) )
        serializers = SearchSerializer(queryset,many=True)
        return Response(serializers.data)
