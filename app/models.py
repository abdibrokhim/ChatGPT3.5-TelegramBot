from django.db import models

# Create your models here.


class TGClient(models.Model):
    tg_id = models.CharField(max_length=255,)
    username = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tg_id


class Pricing(models.Model):
    name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Balance(models.Model):
    tg_id = models.CharField(max_length=255)
    tariff = models.CharField(max_length=255, default='Free Trial')
    next_payment = models.CharField(max_length=255)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.tg_id