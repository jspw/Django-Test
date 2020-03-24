from django.conf.urls import url
from app_template import views


# Template Tagging

app_name = 'template_app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^signup/',views.signupform,name='signup'),
    url(r'^basic/',views.basic,name='basic'),
    url(r'^other/',views.other,name='other'),
    url(r'^relative_template/',views.relateive_template,name='relative_template'),
    url(r'^user_login/$',views.user_login,name='user_login'),


]