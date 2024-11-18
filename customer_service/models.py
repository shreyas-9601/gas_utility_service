from django.db import models

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    attached_file = models.FileField(upload_to='uploads/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service_type}"
