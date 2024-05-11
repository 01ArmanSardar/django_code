
from django.urls import path
from . import views
# from django.contrib.auth.views import LogoutView
urlpatterns = [
   path('register/',views.register,name='register'),
   # path('login/',views.user_login,name='login'),
   path('login/',views.UserLogInView.as_view(),name='login'),
   path('loogout/',views.user_logout,name='logout'),
   # path('logoutt/',views.LogoutView.as_view(),name='logout'),
   path('profile/',views.profile,name='profile'),
   path('Profile/edit/passchange/',views.passChange,name='passchange'),
   path('Profile/edit/',views.editProfile,name='editProfile')

]