from django.urls import path
from . import views
urlpatterns = [
    path('',views.car,name="carpage"),
    path('details/<int:id>/',views.CarDetails.as_view(),name='details')
]