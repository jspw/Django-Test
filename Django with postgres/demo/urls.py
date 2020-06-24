from django.urls import path, re_path
from .views import Index

# app_name = AppName

urlpatterns = [
    path('',Index.as_view(),name="index")
]