from django.urls import path,include
from demo.views import index
from rest_framework import routers
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

#jwt
# from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register('books',BookViewSet)

urlpatterns=[
    path('',index.as_view(),name="index"),
    path('rest/',include(router.urls)),
    path('auth',obtain_auth_token),

    # path('hello/', jwt_views.HelloView.as_view(), name='hello'),
]