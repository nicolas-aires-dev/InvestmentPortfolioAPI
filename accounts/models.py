from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    cash = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        default=0
    )
