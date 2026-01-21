from django.urls import path
from .views import receive_vitals

urlpatterns = [
    path("receive/", receive_vitals),
]
