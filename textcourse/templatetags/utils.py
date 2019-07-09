from django import template
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe 
#form django.template.defaultfilters import linebreaksbr
from django.template.defaultfilters import capfirst, linebreaksbr

register = template.Library()

# @register.filter(name='active')
# def active(inst, user):
#     if user.is_superuser: