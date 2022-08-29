from django.db import models

# Create your models here.
class Blood(models.Model):
    blood_type = models.CharField(max_length=5)
    def __str__(self):
        return self.blood_type