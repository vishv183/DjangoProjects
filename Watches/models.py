from django.db import models
from django.db.models import F
from django.db.models.functions import Now, Pi

# Create your models here.

movement_type = [
    ('Automatic', 'Automatic'),
    ('Manual', 'Manual'),
    ('Quartz', 'Quartz')
]


class Watch(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    case_material = models.CharField(max_length=100)
    strap_material = models.CharField(max_length=100)
    movement_type = models.CharField(max_length=50, choices=movement_type)
    water_resistance = models.CharField(max_length=100)
    case_diameter = models.FloatField()
    case_thickness = models.FloatField()
    bandwidth = models.IntegerField()
    dial_color = models.CharField(max_length=150)
    crystal_material = models.CharField(max_length=100)
    complications = models.CharField(max_length=255)
    power_reserve = models.CharField(max_length =100)
    price = models.FloatField(blank=True, null=True, max_length=100)
    created_at = models.DateTimeField()
    class Meta:
        ordering = ['id']
    def __str__(self):
        return f' {self.id} {self.brand}'

class MyModel(models.Model):
    age = models.IntegerField(db_default=18)
    count = models.IntegerField(default=10)
    created = models.DateTimeField(db_default=Now())
    base = models.FloatField()
    height = models.FloatField()
    area = models.GeneratedField(
        expression=F("base") * F("height"),
        output_field=models.FloatField(),
        db_persist=True,
    )
    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.area}'

SPORT_CHOICES = {  # Using a mapping instead of a list of 2-tuples.
    "Martial Arts": {"judo": "Judo", "karate": "Karate"},
    "Racket": {"badminton": "Badminton", "tennis": "Tennis"},
    "unknown": "Unknown",
}

class Time(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    sport = models.CharField(choices=SPORT_CHOICES, null=True)

