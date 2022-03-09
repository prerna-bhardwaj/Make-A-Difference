from time import time
from django.forms import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
    

class DriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drive
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {
            'password' : {
                'write_only': True,
                'required': True,
            }
        }
    
    def create(self, validated_data):
        print("----", validated_data)
        print(timezone.now())
        user =  User.objects.create_user(username=validated_data['username'],
                                         password=validated_data['password'],
                                         last_login=timezone.now())
        return user