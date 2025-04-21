from django.db import models


class Car(models.Model):
    MAKE_CHOICES = [
        ('Toyota', 'Toyota'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes'),
        ('Audi', 'Audi'),
        ('Other', 'Other'),
    ]

    make = models.CharField(max_length=50, choices=MAKE_CHOICES)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_new = models.BooleanField(default=True)
    configuration = models.TextField(blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({'New' if self.is_new else 'Used'})"
