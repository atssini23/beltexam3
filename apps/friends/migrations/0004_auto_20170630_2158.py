# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 21:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_auto_20170630_2156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='second_friend',
            new_name='secondfriend',
        ),
    ]
