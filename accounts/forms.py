from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Donor, Blood, Patient, Employee, Profile
from django.db import transaction


# Donor Sign Up
class DonorSignUpForm(UserCreationForm):
    queryset = Blood.objects.all()
    # Fields that will appear in the form
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    blood_type = forms.ModelChoiceField(queryset=queryset,widget=forms.RadioSelect())
    phone_number = forms.CharField(required=True)
    donor_location = forms.CharField(required=True)
    
    
    # Model the form data will be saved to
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    # As soon as the form is submitted, the data entered is sent to the database in one transaction.
    @transaction.atomic
    def save(self, *args,**kwargs):
        custom_user = super().save(*args,**kwargs,commit=False)
        custom_user.is_donor = True
        custom_user.first_name = self.cleaned_data.get('first_name')
        custom_user.last_name = self.cleaned_data.get('last_name')
        custom_user.blood_type = self.cleaned_data.get('blood_type')
        custom_user.phone_number=self.cleaned_data.get('phone_number')
        custom_user.save()
        donor = Donor.objects.create(custom_user=custom_user)
        donor.donor_location=self.cleaned_data.get('donor_location')
        donor.save()
        return custom_user



# Donor Login Form
class DonorLoginForm(forms.Form):
    username= forms.CharField(max_length=70)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)


# Patient Sign Up
class PatientSignUpForm(UserCreationForm):
    queryset = Blood.objects.all()
    # Fields that will appear in the form
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    blood_type = forms.ModelChoiceField(queryset=queryset,widget=forms.RadioSelect())
    phone_number = forms.CharField(required=True)
    patient_location = forms.CharField(required=True)
    
    
    # Model the form data will be saved to
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    # As soon as the form is submitted, the data entered is sent to the database in one transaction.
    @transaction.atomic
    def save(self,*args,**kwargs,):
        custom_user = super().save(*args,**kwargs, commit=False)
        custom_user.is_patient = True
        custom_user.first_name = self.cleaned_data.get('first_name')
        custom_user.last_name = self.cleaned_data.get('last_name')
        custom_user.blood_type = self.cleaned_data.get('blood_type')
        custom_user.phone_number=self.cleaned_data.get('phone_number')
        custom_user.save()
        patient = Patient.objects.create(custom_user=custom_user)
        patient.patient_location=self.cleaned_data.get('patient_location')
        patient.save()
        return custom_user



# Patient Login Form
class PatientLoginForm(forms.Form):
    username= forms.CharField(max_length=70)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)


# Patient Sign Up
class EmployeeSignUpForm(UserCreationForm):
    queryset = Blood.objects.all()
    # Fields that will appear in the form
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    blood_type = forms.ModelChoiceField(queryset=queryset,widget=forms.RadioSelect())
    phone_number = forms.CharField(required=True)
    employee_location = forms.CharField(required=True)
    
    
    # Model the form data will be saved to
    class Meta(UserCreationForm.Meta):
        model = CustomUser

    # As soon as the form is submitted, the data entered is sent to the database in one transaction.
    @transaction.atomic
    def save(self,*args,**kwargs,):
        custom_user = super().save(*args,**kwargs,commit=False)
        custom_user.is_patient = True
        custom_user.first_name = self.cleaned_data.get('first_name')
        custom_user.last_name = self.cleaned_data.get('last_name')
        custom_user.blood_type = self.cleaned_data.get('blood_type')
        custom_user.phone_number=self.cleaned_data.get('phone_number')
        custom_user.save()
        employee = Employee.objects.create(custom_user=custom_user)
        employee.employee_location=self.cleaned_data.get('employee_location')
        employee.save()
        return custom_user



# Patient Login Form
class EmployeeLoginForm(forms.Form):
    username= forms.CharField(max_length=70)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = CustomUser
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
