from django.conf.urls import url
from adv_app import views




app_name = 'adv_app'

urlpatterns = [
    url(r'^$',views.SchoolListView.as_view(),name='list'),
    url(r'^$',views.SchoolDetailView.as_view(),name='detail'),

]