from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prof/', views.prof, name='prof'),
    path('chair/', views.chair, name='prof'),
]
