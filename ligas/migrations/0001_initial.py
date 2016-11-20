# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, default='Equipo')),
                ('color', models.CharField(max_length=50, default='Color')),
                ('capitan', models.CharField(max_length=50, default='Capitan')),
                ('comment', models.CharField(max_length=200, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='equipo',
            name='league',
            field=models.ForeignKey(blank=True, to='ligas.Liga', null=True),
        ),
    ]
