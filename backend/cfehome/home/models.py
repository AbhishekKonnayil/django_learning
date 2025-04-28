from django.db import models

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=50)


class Person(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                             related_name='members', null=True, blank=True, default=None)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
