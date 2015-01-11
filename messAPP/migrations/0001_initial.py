# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('userid', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('roll_number', models.CharField(unique=True, max_length=10, blank=True)),
                ('registration_number', models.CharField(unique=True, max_length=10, blank=True)),
                ('current_section', models.CharField(max_length=4)),
                ('current_year', models.CharField(max_length=4)),
                ('joining_year', models.CharField(max_length=4)),
                ('course', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=1)),
                ('email', models.CharField(unique=True, max_length=64)),
                ('country', models.CharField(max_length=32)),
                ('mobile', models.CharField(max_length=16)),
                ('hostel_room', models.CharField(max_length=10)),
                ('hostel', models.CharField(max_length=10)),
                ('mess', models.CharField(max_length=10)),
                ('mess_attendence', models.IntegerField(null=True, blank=True)),
                ('last_checkin', models.TimeField(null=True, blank=True)),
                ('uid', models.IntegerField(null=True, db_column='UID', blank=True)),
            ],
            options={
                'db_table': 'student_data',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
