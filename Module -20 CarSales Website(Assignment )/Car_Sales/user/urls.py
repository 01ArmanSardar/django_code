from django.urls import path
from . import views
urlpatterns = [
    path('',views.user,name="carpage"),
    path('signup/',views.signup,name='signupPage'),
    path('login/',views.userLogin,name='login')
]