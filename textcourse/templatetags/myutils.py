from django import template
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe 
#form django.template.defaultfilters import linebreaksbr
from django.template.defaultfilters import capfirst, linebreaksbr

register = template.Library()

@register.filter(name='previous_active')
def previous_active(inst, user):
    if user and hasattr(user, 'is_superuser') and user.is_superuser:
        return inst.previous
    else:
        if not inst.previous or (inst.previous and inst.previous.active):
            return inst.previous
        else:
            return previous_active(inst.previous, user)

@register.filter(name='next_active')
def next_active(inst, user):    
    if user and hasattr(user, 'is_superuser') and user.is_superuser:
        return inst.next
    else:
        if not inst.next or (inst.next and inst.next.active):
            return inst.next
        else:
            return next_active(inst.next, user)

@register.filter(name='previous_active_url')
def previous_active_url(inst, user):
    if previous_active(inst, user):
        return previous_active(inst, user).get_absolute_url()
    else:
        return ""

@register.filter(name='next_active_url')
def next_active_url(inst, user):    
    if next_active(inst, user):
        return next_active(inst, user).get_absolute_url()
    else:
        return ""         
      