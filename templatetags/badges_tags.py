from django.template import Library

register = Library()

@register.filter
def is_in(value,arg):
   return value in arg

@register.filter
def level_count(badges, level):
   return badges.filter(level=level).count()









