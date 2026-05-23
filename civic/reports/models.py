from django.db import models

# Citizen reports model
class Report(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    location = models.CharField(max_length=50, blank=True)
    gps = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='uploads/', blank=True)