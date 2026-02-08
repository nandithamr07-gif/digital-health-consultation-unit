from django.urls import path
from .views import operator_dashboard
from .views import operator_dashboard, refill_medicine
from . import views


urlpatterns = [
    path('',views.operator_dashboard, name='operator_dashboard'),
    path('operator/refill/<int:med_id>/', refill_medicine, name='refill_medicine'),
]
