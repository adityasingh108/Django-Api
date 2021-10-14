from django.db import router
from django.urls import path,include
import rest_framework
from rest_framework.routers import DefaultRouter
from .import views



router = DefaultRouter()
router.register('userprofile',views.UserProfileViewset,basename='userprofile')
router.register('feed',views.ProfileFedItemViewset)


urlpatterns =[
    path('',include(router.urls)),
    path('login/',views.UserLoginViewset.as_view()),
    path('auth/',include('rest_framework.urls')),
]