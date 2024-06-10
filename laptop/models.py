from django.db import models

# Create your models here.
STORAGE_CHOICES = [
    ('SSD', 'SSD'),
    ('HDD', 'HDD'),
]


class Laptop(models.Model):
    laptop = models.CharField(max_length=256)
    status = models.CharField(max_length=255,null=True, blank=True)
    brand = models.CharField(max_length=150)
    model = models.CharField(max_length=100)
    cpu = models.CharField(max_length=150, null=True, blank=True)
    ram = models.IntegerField()
    Storage = models.IntegerField()
    storage_type = models.CharField(max_length=50, choices=STORAGE_CHOICES)
    gpu = models.CharField(max_length=150)
    screen = models.FloatField(null=True, blank=True)
    touch = models.BooleanField()
    price = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f' {self.id}, {self.laptop}'
