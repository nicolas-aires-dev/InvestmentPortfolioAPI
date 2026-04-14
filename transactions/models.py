from django.db import models
from portfolio.models import Portfolio
from assets.models import Stock


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ("BUY", "Buy"),
        ("SELL", "Sell")
    ]

    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.PROTECT, related_name='transactions')
    stock_id = models.ForeignKey(Stock, on_delete=models.PROTECT, related_name='transactions')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=4, choices=TRANSACTION_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
