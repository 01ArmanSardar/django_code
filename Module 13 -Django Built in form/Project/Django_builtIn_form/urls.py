
from django.urls import path
from . import views
urlpatterns = [
path('',views.home ,name='AppHome'),
path('djangoform/', views.passwordCHeckForm,name='djangoform')
]