from django.forms import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


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
        user =  User.objects.create_user(**validated_data)
        # Token.objects.create(user=user)
        return user