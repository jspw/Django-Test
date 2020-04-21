

from django.urls import path
from django.conf.urls import url,include
from demo.views import index,about,List,Detail,ApiView

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register("info",ApiView)
# app_name = "demo"

urlpatterns = [
    path('',index.as_view(),name="index"),
    path("list/",List.as_view(),name="list"),
    path('about/',about.as_view(),name="about"),
    path('detail/<int:pk>/',Detail.as_view(),name='detail'),
    # rest api 
    path('rest/',include(router.urls)), #this is for the database
    path('auth/',obtain_auth_token), ##Get the token using username and password
]

