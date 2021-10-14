from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views



router = DefaultRouter()
router.register('userprofile',views.UserProfileViewset,basename='userprofile')



urlpatterns =[
    path('',include(router.urls)),
    path('login/',views.UserLoginViewset.as_view()),
]