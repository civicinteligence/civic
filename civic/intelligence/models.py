from django.db import models
from reports.models import Report

# AI results model

class Results(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    urgency = models.CharField(max_length=20)
    location = models.CharField(max_length=50) #if from NLP
    status = models.CharField(max_length=10, default='pending')