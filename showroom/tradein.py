from django.db import models
from django.contrib.auth.models import User
from car import Car


class TradeINDeal(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    old_car_description = models.TextField()
    new_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    valuation = models.DecimalField(max_digits=10, decimal_places=2)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Trade-IN: {self.client.username} -> {self.new_car}"
