# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='course',
        ),
        migrations.AddField(
            model_name='instructor',
            name='data_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='email',
            field=models.EmailField(max_length=254, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(help_text=b'This is name', max_length=255, verbose_name='Instructor Name'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='surname',
            field=models.CharField(max_length=255),
        ),
    ]
