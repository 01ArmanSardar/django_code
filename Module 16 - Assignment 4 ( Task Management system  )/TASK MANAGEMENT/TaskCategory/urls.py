
from django.urls import path
from . import views
urlpatterns = [
    path('',views.TChome,name='tchome')
]