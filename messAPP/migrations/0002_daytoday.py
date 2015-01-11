# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayToDay',
            fields=[
                ('uid', models.CharField(max_length=16, serialize=False, primary_key=True, db_column='UID')),
                ('date', models.DateField(null=True, blank=True)),
                ('break_fast', models.TimeField(null=True, blank=True)),
                ('dinner', models.TimeField(null=True, blank=True)),
                ('lunch', models.TimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'day_to_day',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
