from django.db import models
from accounts.models import User


class Portfolio(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='portfolio')
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
