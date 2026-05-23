from django.db import models
from reports.models import Report

# AI results model

class Issues(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    issue_category = models.CharField(max_length=50)
    location = models.CharField(max_length=50) #If extracted by AI
    sentiment = models.CharField(max_length=20)
    urgency = models.CharField(max_length=20)
    severity = models.CharField(max_length=20)