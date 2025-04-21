from django.db import models
from car import Car


class PriceList(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PriceList for {self.car}"
