"""
Tag model
"""
from uuid import uuid4

from django.db import models


class Tag(models.Model):
    """
    Tag model
    """

    uid = models.UUIDField(verbose_name="UID", help_text="UID", default=uuid4, primary_key=True)
    name = models.CharField(verbose_name="Name", help_text="Name", max_length=250, unique=True)
    description = models.TextField(verbose_name="Description", help_text="Description", blank=True, null=True)

    def __str__(self):
        return self.name
