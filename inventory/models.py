from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    batch_number = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    low_stock_threshold = models.PositiveIntegerField(default=10)
    last_refilled = models.DateTimeField(auto_now=True)

    def is_low_stock(self):
        return self.quantity <= self.low_stock_threshold

    def __str__(self):
        return self.name
