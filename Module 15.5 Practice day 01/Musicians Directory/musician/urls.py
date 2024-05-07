
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name='musucianPage'),
   path('editMusician/<int:id>',views.edit_musician,name='editmusucian')
]