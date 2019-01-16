from django.db import models

# Create your models here.
class Matches(models.Model):
    id = models.IntegerField(primary_key = True)
    season = models.IntegerField(default=0)
    city = models.CharField(max_length = 30)
    date = models.CharField(max_length=30)
    team1 = models.CharField(max_length = 30)
    team2 = models.CharField(max_length = 30)
    toss_winner = models.CharField(max_length = 30)
    toss_decission = models.CharField(max_length = 10)
    result = models.CharField(max_length = 20)
    dl_applied = models.IntegerField(default=0)
    winner = models.CharField(max_length = 30)
    win_by_runs = models.IntegerField(default = 0)
    win_by_wickets = models.IntegerField(default=0)
    player_of_match = models.CharField(max_length = 20)
    venue = models.CharField(max_length = 100)
    umpire1 = models.CharField(max_length = 50)
    umpire2 = models.CharField(max_length = 50)
    umpire3 = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.id)
    
    # class Meta:
    #     managed = False
    #     db_table = 'matches'

class Deliveries(models.Model):
    match = models.ForeignKey(Matches, on_delete=models.CASCADE)
    inning = models.IntegerField(default=0)
    batting_team = models.CharField(max_length = 30)
    bowling_team = models.CharField(max_length = 30)
    over = models.IntegerField(default=0)
    ball = models.IntegerField(default=0)
    batsman = models.CharField(max_length = 30)
    non_striker = models.CharField(max_length = 30)
    bowler = models.CharField(max_length = 30)
    is_super_over = models.IntegerField(default=0)
    wide_runs = models.IntegerField(default=0)
    bye_runs = models.IntegerField(default=0)
    legbye_runs = models.IntegerField(default=0)
    noball_runs = models.IntegerField(default=0)
    batsman_runs = models.IntegerField(default=0)
    penalty_runs = models.IntegerField(default=0)
    extra_runs = models.IntegerField(default=0)
    total_runs = models.IntegerField(default=0)
    player_dismissed = models.CharField(max_length = 20)
    dismissal_kind = models.CharField(max_length = 50)
    fielder = models.CharField(max_length = 30)

    def __str__(self):
        return str(self.match)   
    
    # class Meta:
    #     managed = False
    #     db_table = 'deliveries'