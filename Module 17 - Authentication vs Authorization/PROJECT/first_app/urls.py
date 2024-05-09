from django.urls import path
from . import views
urlpatterns = [
   path('signup/',views.signup,name='signup'),
   path('',views.home,name='home'),
   path('profile/',views.profile,name='profile'),
path('logout/',views.user_log_out,name='logout'),
   path('login/',views.User_login,name='login'),
   path('passchange/',views.pass_change,name='passchange'),
   path('passchange2/',views.pass_change_withoutOLd,name='passchangeWithOUTold')
]