
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Thome,name='thome'),
    path('edit/<int:id>', views.edit,name='editTask'),
    path('delete/<int:id>', views.delete,name='deleteTask')
]