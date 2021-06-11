from django.db.models import fields
from restapi import models
from restapi.models import BookingDetails, Cart, Orders, Products, WorkshopAccount
from django.contrib.auth.models import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password','first_name']
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data.get('username'),
            email = validated_data.get('email'),
            
        )
        
        
        user.set_password(validated_data.get('password'))
        user.save()

        return user


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model= WorkshopAccount
        fields = ['user','workshopName','address','phone','latitude','longitude']




class WorkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name']

class WorkshopWorksSerializers(serializers.ModelSerializer):
    user = WorkUserSerializer()
    class Meta:
        model = BookingDetails
        fields = ['id','created','latitude','longitude','msg','user','status']






######################################################
class ProductSellerName(serializers.Serializer):
    class Meta:
        models = WorkshopAccount
        fields = ('workshopName')

class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.CharField(source='workshop.workshopName')
    class Meta:
        model = Products
        fields = ('id','name','image','price','desc','seller')





class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Cart
        fields = ('id','product')


        
class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()    
    class Meta:
        model = Orders
        fields = ('id','product','status')


class SellerOrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()   
    username = serializers.CharField(source='user.username') 
    class Meta:
        model = Orders
        fields = ('id','product','status','address','latitude','longitude','username')