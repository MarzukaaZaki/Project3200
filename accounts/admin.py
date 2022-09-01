from django.contrib import admin

from accounts.models import CustomUser, Donor, Employee, Patient, Profile

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Employee)
admin.site.register(Donor)
admin.site.register(Patient)
admin.site.register(Profile)
