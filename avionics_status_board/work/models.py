from django.db import models
from users.models import CustomUser
from airplane.models import Airplane  # Updated import

class Work(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(
        max_length=50,
        choices=[
            ("pick_up", "Pick Up"),
            ("flt_sqwk", "Flight Squawk"),
            ("cro", "CRO"),
            ("troubleshooting", "Troubleshooting"),
            ("software", "Software"),
            ("other", "Other"),
        ],
    )
    status = models.CharField(
        max_length=50,
        choices=[
            ("pending", "Pending"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
            ("cant_work", "Can't Work"),
            ("open_paper", "Open Paper"),
        ],
        default="pending",
    )
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)  # Updated reference
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.airplane.line_number}"
