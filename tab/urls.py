from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('edit', views.edit, name='edit'), 
]