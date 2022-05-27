
from . import views
from django.urls import path

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('today/',views.news_of_day,name='newsToday'),
]