try:
    from django.db.models.signals import post_migrate as db_ready
except ImportError:
    from django.db.models.signals import post_syncdb as db_ready


def sync_badges_to_db(**kwargs):
    from .utils import registered_badges
    for badge in registered_badges.values():
        badge.badge


db_ready.connect(sync_badges_to_db)