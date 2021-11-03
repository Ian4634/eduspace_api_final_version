from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('query/', views.query, name = 'query'),
    path('delete/', views.delete, name = 'delete')
    ]

app_name = 'myapp'