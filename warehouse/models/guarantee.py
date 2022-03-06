from django.db import models

class Guarantee(models.Model):
    title = models.CharField(
        'Title',
        max_length=255,
        help_text = 'Title of the guarantee'
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title