from django.db import models
# Create your models here.


class Residence(models.Model):
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()


class Workplace(models.Model):
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    employer_name = models.CharField(max_length=50)
    employer_number = models.IntegerField()
    employer_email = models.CharField(max_length=50)
    title = models.CharField(max_length=50)


# class FunPlace(models.Model):
#     address_line_1 = models.CharField(max_length=100)
#     address_line_2 = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     latitude = models.IntegerField()
#     longitude = models.IntegerField()
