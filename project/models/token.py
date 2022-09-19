"""
Token model
"""
from uuid import uuid4

from django_better_admin_arrayfield.models.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_resized import ResizedImageField
from model_utils.models import TimeStampedModel


class Token(TimeStampedModel):
    """
    Token model
    """

    uid = models.UUIDField(verbose_name="UID", help_text="UID", default=uuid4, primary_key=True)
    name = models.CharField(verbose_name="Name", help_text="Name", max_length=250, unique=True)
    score = models.PositiveIntegerField(
        verbose_name="Score", help_text="Score", default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    blockchain = models.ForeignKey(
        "project.Blockchain", verbose_name="Blockchain", help_text="Blockchain", on_delete=models.CASCADE
    )
    categories = ArrayField(
        models.CharField(max_length=250), verbose_name="Categories", help_text="Categories"
    )
    image = ResizedImageField(verbose_name="Image", help_text="Image", size=[200, 200])
    audit = models.URLField(verbose_name="Audit", help_text="Audit", max_length=1000)
    twitter = models.URLField(verbose_name="Twitter", help_text="Twitter", max_length=1000, blank=True, null=True)
    website = models.URLField(verbose_name="Website", help_text="Website", max_length=1000, blank=True, null=True)
    telegram = models.URLField(verbose_name="Telegram", help_text="Telegram", max_length=1000, blank=True, null=True)
    audit_date = models.DateTimeField(verbose_name="Audit date", help_text="Audit date")
    is_partner = models.BooleanField(verbose_name="Is partner", help_text="Is partner", default=False)
    contract_address = models.CharField(
        verbose_name="Contract address", help_text="Contract address", max_length=250
    )
    index = models.PositiveIntegerField(verbose_name="Index", help_text="Index", blank=True, null=True)

    class Meta:
        ordering = ("-audit_date",)

    def __str__(self):
        return self.name
