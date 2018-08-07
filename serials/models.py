from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

# Create your models here.
class Serial(models.Model):
    title = models.CharField(_('title'), max_length=150, blank=False, null=False)
    abstract = models.TextField(_('abstract'), max_length=500, blank=True, null=True)
    image = models.ImageField(_('image'), upload_to="upload/serial/", blank=True, null=True)
    order = models.IntegerField(_("order"), blank=True, null=True, default=-1)
    active = models.BooleanField(_("active"), default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("serial_detail", kwargs={"pk":self.pk})

    class Meta:
        verbose_name = _("Serial")
        verbose_name_plural = _("Serial")
        ordering = ['order', '-updated']

class Entry(models.Model):
    serial = models.ForeignKey(Serial, verbose_name = _("serial"), blank=False, null=False)
    title = models.CharField(_('title'), max_length=150, blank=False, null=False)
    url = models.URLField(_('url'), max_length=100, blank=False, null=False)
    image = models.ImageField(_('image'), upload_to="upload/serial/", blank=True, null=True)
    order = models.IntegerField(_("order"), blank=True, null=True, default=-1)
    active = models.BooleanField(_("active"), default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("Entry")
        verbose_name_plural = _("Entry")
        ordering = ['order', '-updated']   

from django.db import models
from cms.models import CMSPlugin
from serials.models import Serial


class SerialPluginModel(CMSPlugin):
    serial = models.ForeignKey(Serial)

    def __unicode__(self):
        return self.serial.title             