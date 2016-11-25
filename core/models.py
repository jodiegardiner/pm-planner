from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    notes = models.TextField(default="Enter notes")
    gp = models.CharField(max_length=200, blank=True)
    gp_tel = models.CharField(max_length=15, blank=True)
    hospital = models.CharField(max_length=50, blank=True)
    hospital_num = models.CharField(max_length=50, blank=True)
    dob = models.DateField(default=timezone.now)
    height = models.CharField(max_length=20, blank=True)
    weight = models.CharField(max_length=20, blank=True)
    bmi = models.CharField(max_length=50, blank=True)
    parity = models.CharField(max_length=20, blank=True)
    prev_pregs = models.TextField(max_length=500, blank=True)
    blood_type = models.CharField(max_length=15, blank=True)
    serology = models.CharField(max_length=20, blank=True)
    haemoglobin = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Pregnancy(models.Model):
    client = models.ForeignKey(Client, related_name="pregnancies")
    due_date = models.DateField()
    week_care_commences = models.IntegerField()
    notes = models.TextField(default="Enter notes")
    placental_site = models.CharField(max_length=50, blank=True)
    consultant_clinic = models.CharField(max_length=50, blank=True)
    public_health_nurse = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.client.name


class PregnancyEvent(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, related_name="pregnancy_events")
    title = models.CharField(max_length=50)
    event_date = models.DateTimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title


#
#
# class Event():
#     type foreign key to EventType
#     client
#     notes
#
#
# class EventType():
#     title
#     when
#     description

