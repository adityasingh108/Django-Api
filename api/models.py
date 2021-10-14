from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.conf import settings

# Create your models here.

class UserProfileManager(BaseUserManager):
    ''' create a user profile base manager'''
    def create_user(self,email,name,password=None):
        ''' create a user '''
        if not email:
            raise ValueError('User must have email address')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,password):
        ''' create a super user using  super user'''
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff =True
        user.save(using=self._db)
        return user
        
        


class UserProfile(PermissionsMixin,AbstractBaseUser):
    ''' create a custom user profile  '''
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255 ,unique=True)
    is_active  = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS  = ['name']
    
    def get_full_name(self):
        '''retrive a full name '''
        return self.name
    
    def get_short_name(self):
        '''retrive a short name'''
        self.name
        
    def __str__(self):
        ''' set a static string'''
        return self.name
    
    
class ProfileFedItem(models.Model):
    ''' model for feed the user profile'''
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        '''return a string ''' 
        return self.status_text       