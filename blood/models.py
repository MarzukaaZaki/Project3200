from django.db import models

# Create your models here.
class Blood(models.Model):
    blood_type = models.CharField(max_length=5)
    def __str__(self):
        return self.blood_type

class Blood_Camp(models.Model):
    name_of_camp = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    def __str__(self):
        return self.name_of_camp
