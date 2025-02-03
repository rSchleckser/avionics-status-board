from django.db import models
from users.models import CustomUser

class Airplane(models.Model):  # Placeholder for the Airplane model
    line_number = models.IntegerField(unique=True)
    effectivity = models.IntegerField()
    customer = models.CharField(max_length=255)
    delivered = models.BooleanField(default=False)
    ticketed = models.BooleanField(default=False)

    def __str__(self):
        return f"Line {self.line_number} - {self.customer}"

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
        ]
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
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)  # Ties Work to Airplane
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.airplane.line_number}"


        return f"{self.name} - {self.airplane.line_number}"
