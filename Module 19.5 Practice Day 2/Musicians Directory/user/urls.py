
from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.signupForm,name='signUpForm'),
    path('login/',views.userLogin.as_view(),name='login'),
    path('logout/',views.userLogout,name='logout')
]