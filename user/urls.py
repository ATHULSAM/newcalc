from django.urls import path
from . import views
urlpatterns = [
    path('',views.myfun,name='home'),
    path('test',views.testfun,name='test'),
    path('plants',views.plfun,name='plants'),
    path('staffs',views.stfun,name='staffs'),
    path('login',views.loginfun,name='login'),
    path('dashboard',views.dashfun,name='dashboard'),
    path('bs',views.bsfun,name='bs'),
    path('form',views.formfun,name='form'),
    path('ab',views.abfun,name='ab'),
    path('demo',views.demofun,name='demo'),
    path('fb',views.fbfun,name='fb'),
    path('fb2',views.fb2fun,name='fb2'),
    path('a',views.afun,name='a'),
    path('f',views.ffun,name='f'),
    path('calc',views.calcfun,name='calc')

    
]