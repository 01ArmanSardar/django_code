
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name='albumPage'),
   path('edit/<int:id>',views.editTable,name='edit_table'),
   path('delete/<int:id>',views.delete_table,name='delete_table')
]