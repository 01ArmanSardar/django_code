from django.urls import path
from . import views
urlpatterns = [
    
    path('add_category/',views.add_category,name='category_add'),
    path('Books/',views.book,name='books'),
    path('category/<slug:category_slug>',views.book,name='category_wise_book')
    
]