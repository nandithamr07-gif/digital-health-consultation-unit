from django.db import models

class CallRequest(models.Model):
    patient_id = models.CharField(max_length=20)
    room_name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.patient_id