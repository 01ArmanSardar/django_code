from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('about/',views.about, name='aboutPage'),
    path('submitfrom/', views.submitfrom, name='submitFrom')
]
