from django.db import models

class Color(models.Model):
    title = models.CharField(
        'Color',
        max_length=30,
        help_text = 'Title of the color'
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title