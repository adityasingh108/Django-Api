from django.db import models
from django.db.models import fields
from rest_framework import serializers


from .models import UserProfile,ProfileFedItem




class UserProfileSerializer(serializers.ModelSerializer):
    ''' create a serializer for user profile '''
    class Meta:
        model = UserProfile
        fields = ['id','email','name','password']
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self, validated_data):
        ''' create the user through the api '''
        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
        

class ProfileFedItemSerializer(serializers.ModelSerializer):
    '''create a serializer for ProfileFedItem'''
    user_profile = serializers.StringRelatedField()
    class Meta:
        model = ProfileFedItem
        fields = ['id','user_profile','status_text','created_on']
        extra_kwargs = {'user_profile':{'read_only':True}}

