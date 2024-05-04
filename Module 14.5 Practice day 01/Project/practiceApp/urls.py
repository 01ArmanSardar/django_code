from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='homepage'),
    path('djangoForm/',views.djangoform,name='djangoform'),
    path('ModelForm/',views.modelFields,name='modelfeild'),

]
