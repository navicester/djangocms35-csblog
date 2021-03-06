# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-12 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('textcourse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('abstract', models.TextField(blank=True, max_length=500, null=True, verbose_name='abstract')),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/serial/', verbose_name='image')),
                ('order', models.IntegerField(blank=True, default=-1, null=True, verbose_name='order')),
                ('active', models.BooleanField(default=False, verbose_name='active')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['order', '-updated'],
                'verbose_name': 'Course',
                'verbose_name_plural': 'Course',
            },
        ),
        migrations.AddField(
            model_name='mpttarticle',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='textcourse.Course'),
        ),
    ]
