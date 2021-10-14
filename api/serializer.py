from django.db.models import fields
from rest_framework import serializers


from .models import UserProfile




class UserProfileSerializer(serializers.ModelSerializer):
    ''' create a serializer for user profile '''
    class Meta:
        model = UserProfile
        fields = ['email','name','password']
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
        



