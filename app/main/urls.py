from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('create-schedule/', views.create_schedule, name='create_schedule'),
    path('schedule/', views.schedule, name='schedule'),

    path('block/', views.block, name='block'),

    path('subject/', views.subject, name='subject'),
    path('<int:subj_id>/del_subj/', views.del_subj, name='del_subj'),

    path('room/', views.room, name='room'),
    path('<int:room_id>/del_room/', views.del_room, name='del_room'),

    path('faculty/', views.faculty, name='faculty'),
    path('faculty-form/', views.faculty_form, name='faculty_form'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),

]
