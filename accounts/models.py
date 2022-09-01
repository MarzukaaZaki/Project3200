from django.db import models
from django.contrib.auth.models import AbstractUser
from blood.models import Blood
from PIL import Image

class CustomUser(AbstractUser):
    # Common fields for all types of users
    is_employee = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    blood_type = models.ForeignKey(Blood, on_delete=models.CASCADE, blank=True, null = True)
    def __str__(self):
        return self.first_name
    
class Employee(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)
    designation = models.CharField(max_length=250)
    def __str__(self):
        return f'{self.custom_user.first_name}'
    
class Donor(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)
    donor_location = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.custom_user.first_name}'

class Patient(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)
    patient_location = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.custom_user.first_name}'

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name ='profile')
    image = models.ImageField(default = 'default.png', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
