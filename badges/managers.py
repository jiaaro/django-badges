from django.db import models

class BadgeManager(models.Manager):
    def active(self):
        import badges
        return self.get_queryset().filter(id__in=badges.registered_badges.keys())
        