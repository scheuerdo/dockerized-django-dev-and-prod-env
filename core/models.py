from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):
    """
    Example model for an item.
    This class defines the structure of the Item Table Schema inside the database.
    Each Item has a name and a price.
    """

    name = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(limit_value=0.00)],
    )

    def __str__(self):
        return self.name
