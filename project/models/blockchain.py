"""
Blockchain model
"""
from uuid import uuid4

from django.db import models


class Blockchain(models.Model):
    """
    Blockchain model
    """

    uid = models.UUIDField(verbose_name="UID", help_text="UID", default=uuid4, primary_key=True)
    name = models.CharField(verbose_name="Name", help_text="Name", max_length=250, unique=True)

    def __str__(self):
        return self.name
