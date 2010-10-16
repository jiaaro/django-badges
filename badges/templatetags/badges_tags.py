from django.template import Library
from badges.utils import badge_count
from badges.models import LEVEL_CHOICES
level_choices = dict(LEVEL_CHOICES)

register = Library()

@register.filter
def is_in(value,arg):
   return value in arg

@register.filter
def level_count(badges, level):
   return badges.filter(level=level).count()

@register.filter
def level_title(level):
   return level_choices[level]

@register.filter('badge_count')
def _badge_count(user_or_qs):
   return badge_count(user_or_qs)

