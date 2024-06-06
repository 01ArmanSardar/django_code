from django.urls import path
from .views import UserRegistrationView,UserLogin,UserLogout,UserBankAccountUpdateView
urlpatterns = [
   path('register/',UserRegistrationView.as_view(),name='register'),
   path('login/',UserLogin.as_view(),name='login'),
   path('logout/',UserLogout.as_view(),name='logout'),
   path('editProfile/',UserBankAccountUpdateView.as_view(),name="editProfile")

]