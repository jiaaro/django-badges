from django.db import models

class BadgeManager(models.Manager):
    def active(self):
        from badges.utils import registered_badges
        return self.get_queryset().filter(id__in=registered_badges.keys())
        