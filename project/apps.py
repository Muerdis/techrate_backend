"""
Token config
"""
from django.apps import AppConfig


class ProjectConfig(AppConfig):
    """
    Project module config
    """

    name = "project"

    def ready(self):
        self.verbose_name = "project"
