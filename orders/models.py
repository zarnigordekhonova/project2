from django.db import models

# Create your models here.

class Users_info(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.name} {self.surname}'


class orders(models.Model):
    country = models.CharField(max_length=255)
    ticket_type = models.CharField(max_length=255)
    price = models.IntegerField()
    number_orders = models.IntegerField()


    def __str__(self):
        return f'{self.country} {self.ticket_type}'

