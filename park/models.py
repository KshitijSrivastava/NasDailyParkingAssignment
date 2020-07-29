from django.db import models

# Create your models here.



class CarPark(models.Model):
    car_number = models.CharField(max_length=15)
    park_time = models.DateTimeField(auto_now_add = True)
    # unpark_time = models.DateTimeField(null = True, blank = True)
    active = models.BooleanField()
    slot = models.IntegerField(null = True)

    def __str__(self):
        return self.car_number