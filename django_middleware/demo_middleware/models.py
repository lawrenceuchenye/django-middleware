from django.db import models

# Create your models here.


class UserStat(models.Model):
    android = models.IntegerField()
    desktop = models.IntegerField()
