from django.db import models

# Create your models here.
class Compinfractions(models.Model):
        street = models.CharField(max_length=50)
        speed_limit = models.IntegerField()
        infractions_speed = models.IntegerField()

        def __str__(self):
            return self.street + ' ' + self.speed_limit + ' ' + self.infractions_speed

