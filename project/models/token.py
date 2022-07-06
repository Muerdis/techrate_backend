"""
Token model
"""
from uuid import uuid4

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils.models import TimeStampedModel

from project.enums import BlockchainType


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
        "project.Blockchain", verbose_name="Blockchain", help_text="Blockchain",
        blank=True, null=True, on_delete=models.SET_NULL
    )
    category = models.CharField(verbose_name="Category", help_text="Category", max_length=250)
    image = models.ImageField(verbose_name="Image", help_text="Image")
    audit = models.URLField(verbose_name="Audit", help_text="Audit", max_length=1000)
    twitter = models.URLField(verbose_name="Twitter", help_text="Twitter", max_length=1000, blank=True, null=True)
    website = models.URLField(verbose_name="Website", help_text="Website", max_length=1000, blank=True, null=True)
    audit_date = models.DateTimeField(verbose_name="Audit date", help_text="Audit date")
    is_partner = models.BooleanField(verbose_name="Is partner", help_text="Is partner", default=False)
    contract_address = models.CharField(verbose_name="Contract address", help_text="Contract address", max_length=250)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name
