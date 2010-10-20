from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save

from badges.models import Badge as BadgeModel
from badges.models import BadgeToUser

from django.contrib.auth.models import User

registered_badges = {}

def register(badge):
    if badge.id not in registered_badges:
        registered_badges[badge.id] = badge()
    return badge

def badge_count(user_or_qs=None):
    """
    Given a user or queryset of users, this returns the badge
    count at each badge level that the user(s) have earned.

    Example:

     >>> badge_count(User.objects.filter(username='admin'))
     [{'count': 20, 'badge__level': u'1'}, {'count': 1, 'badge__level': u'2'}, {'count': 1, 'badge__level': u'3'}]

    Uses a single database query.
    """
    kwargs = {}
    if user_or_qs is None:
        pass
    elif isinstance(user_or_qs, User):
        kwargs.update(dict(user=user_or_qs))
    else:
        kwargs.update(dict(user__in=user_or_qs))

    return BadgeToUser.objects.filter(
        **kwargs
    ).values(
        'badge__level',
    ).annotate(
        count=models.Count('badge__level'),
    ).order_by('badge__level')

class MetaBadgeMeta(type):
    
    def __new__(cls, name, bases, attrs):
        new_badge = super(MetaBadgeMeta, cls).__new__(cls, name, bases, attrs)
        parents = [b for b in bases if isinstance(b, MetaBadgeMeta)]
        if not parents:
            # If this isn't a subclass of MetaBadge, don't do anything special.
            return new_badge
        return register(new_badge)


class MetaBadge(object):
    __metaclass__ = MetaBadgeMeta
    
    one_time_only = False
    model = models.Model
    
    def __init__(self):
        # whenever the server is reloaded, the badge will be initialized and
        # added to the database
        self._keep_badge_updated()
        post_save.connect(self._signal_callback, sender=self.model)
    
    def _signal_callback(self, **kwargs):
        i = kwargs['instance']
        self.award_ceremony(i)
    
    def _test_conditions(self, instance):
        condition_callbacks = [getattr(self, c) for c in dir(self) if c.startswith('check')]
        
        # will return False on the first False condition
        return all( fn(instance) for fn in condition_callbacks )
    
    def get_user(self, instance):
        return instance.user
    
    def _keep_badge_updated(self):
        if getattr(self, 'badge', False):
            return False
        badge, created = BadgeModel.objects.get_or_create(id=self.id)
        if badge.level != self.level:
            badge.level = self.level
            badge.save()
        self.badge = badge
    
    def award_ceremony(self, instance):
        if self._test_conditions(instance):
            user = self.get_user(instance)
            self.badge.award_to(user)
