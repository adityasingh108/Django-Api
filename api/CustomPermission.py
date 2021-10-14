from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS, BasePermission


class UpdateOwnProfile(BasePermission):
    ''' update own user profile '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id ==request.user.id
        