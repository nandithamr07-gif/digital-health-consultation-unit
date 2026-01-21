from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.doctor_login, name='doctor_login'),
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('latest-vitals/', views.get_latest_vitals, name='latest_vitals'),

    # ✅ NEW PATH FOR MEDICINE DISPENSING
    path('dispense/', views.dispense_medicine, name='dispense_medicine'),
    path("check-call/", views.check_call),
]