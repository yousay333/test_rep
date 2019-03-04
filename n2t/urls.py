from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('n2t/new/', views.note_new, name='note_new'), 
    path('n2t/tab/', views.note_tab, name='note_tab'), 
]