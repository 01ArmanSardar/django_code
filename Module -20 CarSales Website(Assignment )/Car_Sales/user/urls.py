from django.urls import path
from . import views
urlpatterns = [
    path('',views.user,name="carpage"),
    path('signup/',views.signup,name='signupPage'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),
    path('profile_EditProfile',views.editProfile,name='editProfile')
]