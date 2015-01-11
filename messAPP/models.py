# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class StudentData(models.Model):
    userid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    roll_number = models.CharField(unique=True, max_length=10, blank=True)
    registration_number = models.CharField(unique=True, max_length=10, blank=True)
    current_section = models.CharField(max_length=4)
    current_year = models.CharField(max_length=4)
    joining_year = models.CharField(max_length=4)
    course = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    email = models.CharField(unique=True, max_length=64)
    country = models.CharField(max_length=32)
    mobile = models.CharField(max_length=16)
    hostel_room = models.CharField(max_length=10)
    hostel = models.CharField(max_length=10)
    mess = models.CharField(max_length=10)
    mess_attendence = models.IntegerField(blank=True, null=True)
    last_checkin = models.TimeField(blank=True, null=True)
    uid = models.IntegerField(db_column='UID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name
        
    
    class Meta:
        managed = True
        db_table = 'student_data'

class DayToDay(models.Model):
    uid = models.CharField(db_column='UID', primary_key=True, max_length=16)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    break_fast = models.TimeField(blank=True, null=True)
    dinner = models.TimeField(blank=True, null=True)
    lunch = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.uid
    
    class Meta:
        managed = True
        db_table = 'day_to_day'

