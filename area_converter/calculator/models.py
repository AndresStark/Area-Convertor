from django.db import models

class Number(models.Model):
    square_vars = models.IntegerField(default=0)
    meters = models.IntegerField(default=0)
    foot = models.IntegerField(default=0)
    apples = models.IntegerField(default=0)
    acres = models.IntegerField(default=0)
    hectarea = models.IntegerField(default=0)
