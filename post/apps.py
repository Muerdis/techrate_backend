"""
Tender config
"""
from django.apps import AppConfig


class PostConfig(AppConfig):
    """
    Post module config
    """

    name = "post"

    def ready(self):
        self.verbose_name = "post"
