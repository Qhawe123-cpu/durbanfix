from django.db import models

# Create your models here.
from django.db import models

class Report(models.Model):
    ISSUE_TYPES = [
        ('water', 'Water Issue'),
        ('electricity', 'Electricity Issue'),
        ('roads', 'Road Issue'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPES)
    location = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.issue_type} - {self.location}"