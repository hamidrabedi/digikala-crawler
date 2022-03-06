from django.db import models
from django.core.validators import(
    MinValueValidator,
)

class Pack(models.Model):
    price =models.IntegerField(
        "Sell Price",
        help_text="The price of selling this Pack.",
        validators=[
            MinValueValidator(5000)
        ]
    )

    product = models.ForeignKey(
        'Product',
        verbose_name="Product",
        related_name='packs',
        on_delete=models.CASCADE
    )

    guarantee = models.ForeignKey(
        'Guarantee',
        verbose_name="Guarantee",
        related_name="packs",
        on_delete=models.CASCADE
    )

    color = models.ForeignKey(
        'Color',
        verbose_name="Color",
        related_name="packs",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.price)

    def __repr__(self):
        return str(self.price)