from django.db import models

class PatientReading(models.Model):
    temperature = models.FloatField()
    pulse = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Temp: {self.temperature}, Pulse: {self.pulse} @ {self.timestamp}"

