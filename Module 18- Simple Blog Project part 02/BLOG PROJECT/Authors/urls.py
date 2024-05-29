
from django.urls import path
from . import views
urlpatterns = [
   path('register/',views.register,name='register'),
   path('login/',views.user_login,name='login'),
   path('loogout/',views.user_logout,name='logout'),
   path('profile/',views.profile,name='profile'),
   path('Profile/edit/passchange/',views.passChange,name='passchange'),
   path('Profile/edit/',views.editProfile,name='editProfile')

]