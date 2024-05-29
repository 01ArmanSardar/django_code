from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('',views.home,name='app_home'),
    path('',views.set_session),
    path('gets/',views.get_session,name='session'),
    path('get/',views.get_cookie,name='cookie'),
    path('delete/',views.delete_cookie,name='deleteCookie'),
    path('deletes/',views.delete_session,name='deleteCookie')
    
]
