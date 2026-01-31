from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields can be added here
    pass

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField('User', related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    calories = models.PositiveIntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.ManyToManyField('User', related_name='suggested_workouts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class LeaderboardEntry(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True)
    score = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'team')
