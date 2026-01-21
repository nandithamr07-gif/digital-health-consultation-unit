from django.db import models

class Vitals(models.Model):
    patient_id = models.CharField(max_length=50)
    temperature = models.FloatField(null=True, blank=True)
    pulse = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_id} - {self.timestamp}"
