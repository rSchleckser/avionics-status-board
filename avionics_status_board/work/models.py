from django.db import models
from django.utils.timezone import now
from users.models import CustomUser
from airplane.models import Airplane

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

    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_at = models.DateTimeField(null=True, blank=True)  # Track when assigned

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """Automatically update assigned_at when assigned_to changes."""
        if self.assigned_to and not self.assigned_at:  # Only set if it's assigned for the first time
            self.assigned_at = now()
        elif not self.assigned_to:  # Reset if unassigned
            self.assigned_at = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.airplane.line_number}"
