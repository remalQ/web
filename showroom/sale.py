from django.db import models
from django.contrib.auth.models import User
from car import Car


class Sale(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_tradein = models.BooleanField(default=False)
    contract_file = models.FileField(upload_to='contracts/', null=True, blank=True)

    def __str__(self):
        return f"Sale of {self.car} to {self.client.username}"
