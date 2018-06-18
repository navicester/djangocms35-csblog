from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_out
from django.db.models.signals import post_save


class TrackingConfig(AppConfig):

    name = 'tracking2'
    verbose_name = 'django-tracking2'

    def ready(self):
        from tracking2 import handlers
        from tracking2.models import Visitor
        user_logged_out.connect(handlers.track_ended_session)
        post_save.connect(handlers.post_save_cache, sender=Visitor)
