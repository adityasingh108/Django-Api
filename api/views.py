from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .models import UserProfile,ProfileFedItem
from .CustomPermission import UpdateOwnProfile,UpdateOwnFeed
from .serializer import UserProfileSerializer,ProfileFedItemSerializer

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
    
    
class ProfileFedItemViewset(ModelViewSet):
    '''user feed viewset'''
    queryset = ProfileFedItem.objects.all()
    serializer_class = ProfileFedItemSerializer 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,UpdateOwnFeed]   
    
    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)
    
    