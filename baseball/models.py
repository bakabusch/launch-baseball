from django.db import models

class Batter(models.Model):
    player = models.CharField(max_length=100)
    year = models.IntegerField()
    era = models.CharField(max_length=50)
    gp = models.IntegerField()
    pa = models.IntegerField()
    ba = models.DecimalField(max_digits=3,decimal_places=3, default=0)
    ops = models.DecimalField(max_digits=4,decimal_places=3, default=0)
    single = models.IntegerField()
    two = models.IntegerField()
    three = models.IntegerField()
    hr = models.IntegerField()
    bb = models.IntegerField()
    ibb = models.IntegerField(default=0)
    runs = models.IntegerField()
    rbi = models.IntegerField()
    steals = models.IntegerField()
    ubr = models.DecimalField(max_digits=4,decimal_places=2, default=0)
    wgdp = models.DecimalField(max_digits=3,decimal_places=3, default=0)
    sf = models.IntegerField(default=0)
    hbp = models.IntegerField(default=0)
    wrcplus = models.IntegerField(default=100)


    def __str__(self): #A string representation of this object
        return str(self.year) + "  " + self.player + "  wRC'+'" + str(self.wrcplus)

"""
the big mistake I think I made was not having a player class and a Seasons class. Player would just be player name,
years, teams, and eras they played for(and possibly career stat line) while Seasons would hold individual seasons stats
on a foreign key driven by the player class.
"""