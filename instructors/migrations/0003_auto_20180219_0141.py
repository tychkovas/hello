# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_auto_20180219_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='course',
            field=models.CharField(max_length=255, null=b'True'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
