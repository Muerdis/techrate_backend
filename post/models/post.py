"""
Post model
"""
from uuid import uuid4

from django.db import models
from model_utils.models import TimeStampedModel


class Post(TimeStampedModel):
    """
    Post model
    """

    uid = models.UUIDField(verbose_name="UID", help_text="UID", default=uuid4, primary_key=True)
    name = models.CharField(verbose_name="Name", help_text="Name", max_length=250, unique=True)
    text = models.TextField(verbose_name="Text", help_text="Text", blank=True, null=True)
    image = models.ImageField(verbose_name="Image", help_text="Image", blank=True, null=True)
    tags = models.ManyToManyField("post.Tag", verbose_name="tags")

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name
