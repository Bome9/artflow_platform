from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('publications/', views.publications, name='publications'),
    path('settings/', views.settings, name='settings'),
]
