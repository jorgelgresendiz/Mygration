from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Conneticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IA', 'IOWA'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming')
)


class Residence(models.Model):
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(
        max_length=2,
        choices=STATES
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # route to specific residence card
    def get_absolute_url(self):
        return reverse('residences_detail', kwargs={'residence_id': self.id})

    def
    # class Meta:
    #     order = ['-date']


class Workplace(models.Model):
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(
        max_length=2,
        choices=STATES
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    employer_name = models.CharField(max_length=50, blank=True)
    employer_number = models.CharField(max_length=50, blank=True)
    employer_email = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # route to specific workplace card
    def get_absolute_url(self):
        return reverse('workplaces_detail', kwargs={'workplace_id': self.id})

    # class Meta:
    #     order = ['-date']

    # class FunPlace(models.Model):
    #     address_line_1 = models.CharField(max_length=100)
    #     address_line_2 = models.CharField(max_length=100)
    #     city = models.CharField(max_length=50)
    #     latitude = models.FloatField()
    #     longitude = models.FloatField()
