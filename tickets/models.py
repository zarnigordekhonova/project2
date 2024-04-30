from django.db import models

# Create your models here.


class tickets_info(models.Model):
    type_ticket1 = models.CharField(max_length=255)
    price_ticket1 = models.IntegerField()
    type_ticket2 = models.CharField(max_length=255)
    price_ticket2 = models.IntegerField()


    def __str__(self):
        return f"{self.type_ticket1} {self.price_ticket1}"



class available_tickets(models.Model):
    country_name = models.CharField(max_length=255)
    number_econom_tickets = models.IntegerField()
    number_business_tickets = models.IntegerField()


    def __str__(self):
        return f'{self.country_name} {self.number_econom_tickets}'