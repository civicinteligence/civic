from django.db import models
from django.contrib.auth.models import AbstractUser


class OfficeUser(AbstractUser):
    office_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True)
    issue_category = models.CharField(max_length=15)
    confirm_password = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.username} {self.issue_category}'