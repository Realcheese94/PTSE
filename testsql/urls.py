from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    url(r'^$',views.index, name='index'),
    url(r'^loginuser$',views.loginuser,name='loginuser'),
    url(r'^logout$',auth_views.logout,{'next_page' : '/'}),
    url(r'^register$',views.registuser,name='register'),
    url(r'^registcheck$',views.registercheck,name='registcheck'),              
]