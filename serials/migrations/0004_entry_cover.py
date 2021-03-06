# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-05 16:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('serials', '0003_auto_20180807_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='cover',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='serial_cover', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
