from django.db.models.signals import post_save
from django.db import models
from django.core.urlresolvers import reverse
from models import Badge as BadgeModel
from models import BadgeToUser


class MetaBadge(object):
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

registered_badges = {}

def register(badge): 
    if not registered_badges.has_key(badge.id):
        registered_badges[badge.id] = badge()
    return badge
    