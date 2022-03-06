from django.db import models
from django.core.validators import(
    MinValueValidator,
    MaxValueValidator
)

class Product(models.Model):
    title = models.CharField(
        'Title',
        max_length=100,
        help_text = 'Title of the product',
        unique=True
        )

    subtitle=models.CharField(
        'Subtitle',
        max_length=250,
        help_text = 'Subtitle of the product',
    )

    description = models.TextField(
        'Description',
        help_text = 'Description of the product',
    )

    sku = models.CharField(
        "Stock Unit",
        max_length=13,
        help_text = "An alternative field to store a unique identity for each Object.",
        unique = True,
        editable = False
    )

    rating= models.FloatField(
        'Rating',
        help_text = 'rating of the product',
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )

    # def save(self, *args, **kwargs):
    #     sku = "".join(random.sample("123456789"*3, k=7))
    #     if not self.sku:
    #         self.sku = "digi-{}".format(sku)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title