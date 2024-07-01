from django.urls import path
from . import views
urlpatterns = [
    path('books/',views.BookView.as_view(),name='Book'),
    path('add_category/',views.add_category,name='category_add')
    
]