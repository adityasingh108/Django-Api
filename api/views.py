from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from .models import UserProfile
from .CustomPermission import UpdateOwnProfile
from .serializer import UserProfileSerializer

# Create your views here.


class UserProfileViewset(ModelViewSet):
    ''' userprofile view set'''
    queryset = UserProfile.objects.all()
    serializer_class=UserProfileSerializer
    permission_classes = [UpdateOwnProfile]
    authentication_classes=[TokenAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['name','email']
    
class UserLoginViewset(ObtainAuthToken):
    ''' user login viewset'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
    