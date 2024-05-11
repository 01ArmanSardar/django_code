from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name='app_home'),
   path('signup/',views.signup,name='signup'),
   path('login/',views.user_login,name='login'),
   path('logout/',views.UserLogout,name='logout'),
   path('profile/',views.profile,name='profile')
]