from django.db import models

class Airplane(models.Model):
    line_number = models.PositiveIntegerField(unique=True)
    effectivity = models.PositiveIntegerField()
    customer = models.CharField(max_length=255)
    delivered = models.BooleanField(default=False)
    ticketed = models.BooleanField(default=False)

    def __str__(self):
        return f"Line {self.line_number} - {self.customer}"
