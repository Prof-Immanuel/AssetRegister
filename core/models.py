from django.db import models

# Create your models here.

class StolenItem(models.Model):
    item_name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} ({self.serial_number}) - {self.brand}"
