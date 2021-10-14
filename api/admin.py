from django.contrib import admin
from .models import UserProfile,ProfileFedItem

class UserProfileAdmin(admin.ModelAdmin):
    list_display=['email','name']
    
    
    
admin.site.register(UserProfile ,UserProfileAdmin)
admin.site.register(ProfileFedItem)


