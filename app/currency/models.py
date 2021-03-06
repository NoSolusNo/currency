from django.db import models


class Rate(models.Model):
    bank = models.CharField(max_length=30)
    type = models.CharField(max_length=5)  # eur, usd, rur, uah
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    create = models.DateTimeField()


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=250)
    subject = models.CharField(max_length=300)
    message = models.TextField()
