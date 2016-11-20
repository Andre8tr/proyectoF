# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ligas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='liga',
            name='numero',
            field=models.CharField(default='20', max_length=2),
        ),
        migrations.AddField(
            model_name='liga',
            name='pais',
            field=models.CharField(default='/', max_length=50),
        ),
    ]
