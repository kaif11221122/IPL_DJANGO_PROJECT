from operator import mod, truediv
from pickle import TRUE
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db import models

# # Create your models here.


class Matches(models.Model):

    id = models.IntegerField(primary_key=True)
    season = models.CharField(max_length=40, null=True, default=0)
    city = models.CharField(max_length=25)
    date = models.DateField(null=True)
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    toss_winner = models.CharField(max_length=50)
    toss_decision = models.CharField(max_length=20)
    result = models.CharField(max_length=20)
    dl_applied = models.IntegerField(null=True, default=0)
    winner = models.CharField(max_length=50)
    win_by_runs = models.IntegerField(null=True, default=0)
    win_by_wickets = models.IntegerField(null=True, default=0)
    player_of_match = models.CharField(max_length=40)
    venue = models.CharField(max_length=100)
    umpire1 = models.CharField(max_length=40)
    umpire2 = models.CharField(max_length=40)
    umpire3 = models.CharField(max_length=40)


class Deliveries(models.Model):

    match_id = models.ForeignKey(Matches, on_delete=models.CASCADE)
    inning = models.IntegerField(null=True, default=0)
    batting_team = models.CharField(max_length=50)
    bowling_team = models.CharField(max_length=50)
    over = models.IntegerField(null=True, default=0)
    ball = models.IntegerField(null=True, default=0)
    batsman = models.CharField(max_length=40)
    non_striker = models.CharField(max_length=40)
    bowler = models.CharField(max_length=40)
    is_super_over = models.IntegerField(null=True, default=0)
    wide_runs = models.IntegerField(null=True, default=0)
    bye_runs = models.IntegerField(null=True, default=0)
    legbye_runs = models.IntegerField(null=True, default=0)
    noball_runs = models.IntegerField(null=True, default=0)
    penalty_runs = models.IntegerField(null=True, default=0)
    batsman_runs = models.IntegerField(null=True, default=0)
    extra_runs = models.IntegerField(null=True, default=0)
    total_runs = models.IntegerField(null=True, default=0)
    player_dismissed = models.CharField(max_length=40)
    dismissal_kind = models.CharField(max_length=30)
    fielder = models.CharField(max_length=40)

    # match_id = models.OneToOneField(MatchesDataModel, on_delete=CASCADE)
    # id = models.IntegerField(primary_key=True)
