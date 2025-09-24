from django.db import models
from django.contrib.auth.models import User

class BudgetAlert(models.Model):
    NOTIFICATION_CHOICES = [
        ('dashboard', 'Dashboard'),
        ('email', 'Email'),
        ('push', 'Push Notification'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('warning', 'Warning'),
        ('inactive', 'Inactive'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount_limit = models.DecimalField(max_digits=10, decimal_places=2)
    trigger_threshold = models.PositiveIntegerField(help_text="Percentage of budget")
    notifications = models.JSONField(default=list)  # stores multiple selections
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount_limit}"


# Create your models here.
