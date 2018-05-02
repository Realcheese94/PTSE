from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    url(r'^$',views.index, name='index'),
    url(r'^loginuser$',views.loginuser,name='loginuser'),
    url(r'^logout$',auth_views.logout,{'next_page' : '/'}),
    url(r'^registcheck$',views.registercheck,name='registcheck'),        
    url(r'^registuser$',views.registuser,name='registuser'),
    url(r'^schedule$',views.Schedules,name="Schedule"),
    url(r'^information$',views.Informations, name ='information'),          
]