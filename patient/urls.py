# patient/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('consult/', views.instructions, name='instructions'),
    path('readings/', views.simulate_readings, name='simulate_readings'),
    path('video-call/', views.video_call, name='video_call'),

]
