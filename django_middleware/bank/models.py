from django.db import models

# Create your models here.


class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    e_signature = models.CharField(max_length=255, null=True, blank=True)
    pin = models.IntegerField()
    balance = models.DecimalField(
        max_digits=100, decimal_places=100, default=1000)
    basic_info = models.TextField()


class ETranzact(models.Model):
    from_creditor = models.CharField(max_length=255)
    to_creditee = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
