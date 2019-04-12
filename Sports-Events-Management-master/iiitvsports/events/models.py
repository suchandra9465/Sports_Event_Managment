from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

class Event(models.Model):
    title = models.CharField(max_length=250)
    event_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events:event_list")

class Cricket(models.Model):
    created_by = models.ForeignKey(User,related_name='crickets')
    event = models.ForeignKey('Event',related_name='crickets')
    created_at = models.DateTimeField(auto_now=True)
    team_name = models.CharField(max_length=50)
    Player1 = models.CharField(max_length=50)
    Player2 = models.CharField(max_length=50)
    Player3 = models.CharField(max_length=50)
    Player4 = models.CharField(max_length=50)
    Player5 = models.CharField(max_length=50)
    Player6 = models.CharField(max_length=50)
    Player7 = models.CharField(max_length=50)
    Player8 = models.CharField(max_length=50)
    Player9 = models.CharField(max_length=50)
    Player10 = models.CharField(max_length=50)
    Player11 = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name

    def get_absolute_url(self):
        return reverse('events:event_list')

class Football(models.Model):
    created_by = models.ForeignKey(User,related_name='footballs')
    event = models.ForeignKey(Event,related_name='footballs')
    created_at = models.DateTimeField(auto_now=True)
    team_name = models.CharField(max_length=50)
    Player1 = models.CharField(max_length=50)
    Player2 = models.CharField(max_length=50)
    Player3 = models.CharField(max_length=50)
    Player4 = models.CharField(max_length=50)
    Player5 = models.CharField(max_length=50)
    Player6 = models.CharField(max_length=50)
    Player7 = models.CharField(max_length=50)
    Player8 = models.CharField(max_length=50)
    Player9 = models.CharField(max_length=50)
    Player10 = models.CharField(max_length=50)
    Player11 = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name

    def get_absolute_url(self):
        return reverse('events:event_list')
