from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('consult/', views.instructions, name='instructions'),

    # ✅ Live vitals routes
    path('readings/', views.patient_dashboard, name='patient_dashboard'),
    path('live-vitals/', views.patient_live_vitals, name='patient_live_vitals'),
   
    # ✅ Call trigger
    path('start-call/', views.start_call,name='start_call'),

     # ✅ Video call
    path('video-call/', views.video_call, name='video_call'),

]