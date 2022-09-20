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
    if not created:
        return

    tokens = Token.objects.all()
    index = 0
    for token in tokens:
        index += 1
        token.index = index
        token.save()
