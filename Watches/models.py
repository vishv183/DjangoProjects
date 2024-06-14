from django.utils import timezone

from django.db import models
from import_export import resources

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
    price = models.CharField(blank=True, null=True, max_length=100)
    created_at = models.DateTimeField()
    class Meta:
        ordering = ['id']

    def __str__(self):
        return f' {self.id} {self.brand}'


