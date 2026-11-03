from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    year = models.IntegerField()
    engine = models.CharField(max_length=50, blank=True, null=True)     # Məsələn: 2.0 L
    mileage = models.IntegerField(blank=True, null=True)                # Yürüş (km)
    transmission = models.CharField(max_length=50, blank=True, null=True) # Sürətlər qutusu (Avtomat / Mexanika)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return self.title