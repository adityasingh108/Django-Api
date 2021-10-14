from rest_framework import permissions
from rest_framework.permissions import  BasePermission


class UpdateOwnProfile(BasePermission):
    ''' update own user profile '''
    def has_object_permission(self, request, view, obj):
        '''permission to its own profile '''
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id ==request.user.id


class UpdateOwnFeed(BasePermission):
    ''' custom update own feed '''
    def has_object_permission(self,request,view,obj):
        '''permission to its own feed ''' 
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id       