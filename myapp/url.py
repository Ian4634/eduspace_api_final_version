from django.urls import path
from . import views
urlpatterns = [
    path('', views.query, name = 'query'),
    path('create/', views.index, name = 'index'),
    path('delete/', views.delete, name = 'delete'),
    path('edit/', views.edit , name = 'edit',)
    ]

app_name = 'myapp'