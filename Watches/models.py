from django.db import models

# Create your models here.

movement_type = [
    ('Automatic', 'Automatic'),
    ('Manual', 'Manual'),
    ('Quartz', 'Quartz')
]
class Watch(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255, blank=True, null=True)
    case_materal = models.CharField(max_length=100)
    strap_material = models.CharField(max_length=100)
    movement_type = models.CharField(50, choices=movement_type)
    water_resistance = models.IntegerField(null=True, blank=True)
    case_diameter = models.IntegerField(blank=True, null=True)
    case_thickness = models.IntegerField(blank=True, null=True)
    bandwidth = models.IntegerField(blank=True, null=True)
    dial_color = models.CharField(max_length=150)
    crystal_material = models.CharField(max_length=100)
    complications = models.CharField(max_length=255, blank=True, null=True)
    power_reserve = models.IntegerField()
    price = models.FloatField()



