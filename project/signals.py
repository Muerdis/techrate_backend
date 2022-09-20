"""
Project signals
"""
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from project.models import Token


@receiver(post_save, sender=Token)
def add_indexes_for_tokens(sender, instance, created, **kwargs):  # pylint: disable=unused-argument
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


@receiver(post_delete, sender=Token)
def update_indexes_for_tokens(sender, instance, *args, **kwargs):
    tokens = Token.objects.all()
    index = 0
    for token in tokens:
        index += 1
        token.index = index
        token.save()
