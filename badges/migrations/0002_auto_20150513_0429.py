# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('badges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('level', models.CharField(max_length=1, choices=[('1', 'Bronze'), ('2', 'Silver'), ('3', 'Gold'), ('4', 'Diamond')])),
                ('icon', models.ImageField(upload_to='badge_images')),
            ],
        ),
        migrations.CreateModel(
            name='BadgeToUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('badge', models.ForeignKey(to='badges.Badge')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='badge',
            name='user',
            field=models.ManyToManyField(related_name='badges', through='badges.BadgeToUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
