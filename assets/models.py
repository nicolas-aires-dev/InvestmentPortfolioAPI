from django.db import models


class Stock(models.Model):
    name = models.CharField(null=False, blank=False, max_length=55)
    ticker = models.CharField(null=False, blank=False, max_length=55)
    last_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name