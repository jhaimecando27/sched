from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('schedules/', views.schedules, name='schedules'),
    path('department/', views.department, name='department'),
    path('faculty/', views.faculty, name='faculty'),
    path('faculty-form/', views.faculty_form, name='faculty form'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),
]
