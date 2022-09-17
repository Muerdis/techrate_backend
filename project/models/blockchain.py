"""
Blockchain model
"""
from uuid import uuid4

from django.db import models
from django_resized import ResizedImageField


class Blockchain(models.Model):
    """
    Blockchain model
    """

    uid = models.UUIDField(verbose_name="UID", help_text="UID", default=uuid4, primary_key=True)
    name = models.CharField(verbose_name="Name", help_text="Name", max_length=250, unique=True)
    image = ResizedImageField(verbose_name="Image", help_text="Image", size=[200, 200], blank=True, null=True)
    link = models.URLField(verbose_name="Link", help_text="Link", max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
