"""
Project signals
"""
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from project.models import Token


@receiver(post_save, sender=Token)
def add_index_for_token(sender, instance, created, **kwargs):  # pylint: disable=unused-argument
    """
    Add index for token
    """
    # Token.objects.all().update(index=F('index') + 1)
