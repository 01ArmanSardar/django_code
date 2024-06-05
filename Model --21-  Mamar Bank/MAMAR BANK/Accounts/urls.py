from django.urls import path
from .views import UserRegistrationView,UserLogin,UserLogout
urlpatterns = [
   path('register/',UserRegistrationView.as_view(),name='register'),
   path('login/',UserLogin.as_view(),name='login'),
   path('logout/',UserLogout.as_view(),name='logout'),


]