from django.db import models

class Airplane(models.Model):
    CITY_CHOICES = [
        ("renton","Renton"),
        ("seattle", "Seattle"),
        ("everett", "Everett"),
        ("moses_lake", "Moses Lake"),
        ("victorville", "Victorville"),
        ("portland", "Portland"),
        ("china", "China"),
        ("other", "Other"),
    ]

    STALL_CHOICES = [
        ("C3", "C3"), ("C4", "C4"), ("C5", "C5"), ("C6", "C6"), ("C7", "C7"), ("C8", "C8"), ("C9", "C9"), ("C10", "C10"),
        ("C11", "C11"), ("C12", "C12"), ("C13", "C13"), ("C14", "C14"), ("C15", "C15"), ("C16", "C16"), ("C17", "C17"), ("C18", "C18"), ("C19", "C19"), ("C20", "C20"),
        ("B3", "B3"), ("B4", "B4"), ("B5", "B5"), ("B6", "B6"), ("B7", "B7"), ("B8", "B8"), ("B9", "B9"), ("B10", "B10"),
        ("B11", "B11"), ("B12", "B12"), ("B13", "B13"), ("B14", "B14"), ("B15", "B15"), ("B16", "B16"),
        ("B3N", "B3N"), ("B3S", "B3S"), ("B4N", "B4N"), ("B4S", "B4S")
    ]

    line_number = models.PositiveIntegerField(unique=True)
    effectivity = models.PositiveIntegerField()
    location_city = models.CharField(max_length=50, choices=CITY_CHOICES, default = 'seattle')
    location_stall = models.CharField(max_length=10, choices=STALL_CHOICES, blank=True, null=True)
    customer = models.CharField(max_length=255)
    delivered = models.BooleanField(default=False)
    ticketed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Line {self.line_number} - {self.customer} - {self.location_city} - {self.location_stall} "

