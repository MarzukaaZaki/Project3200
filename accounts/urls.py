from django.urls import path
from accounts.views import (
    DonorRegisterView,RegisterView, DonorLoginView, donor_logout, 
    PatientLoginView, PatientRegisterView, patient_logout, 
    EmployeeRegisterView, EmployeeLoginView, employee_logout, profile)

urlpatterns = [
    path('register/',RegisterView.as_view(),name= 'register'),
    path('donor_register',DonorRegisterView.as_view(), name='donor_register'),
    path('donor_login', DonorLoginView.as_view() , name='donor_login'),
    path('donor_logout', donor_logout , name='donor_logout'),

    
    path('patient_register',PatientRegisterView.as_view(), name='patient_register'),
    path('patient_login', PatientLoginView.as_view() , name='patient_login'),
    path('patient_logout', patient_logout , name='patient_logout'),

    path('employee_register',EmployeeRegisterView.as_view(), name='employee_register'),
    path('employee_login', EmployeeLoginView.as_view() , name='employee_login'),
    path('employee_logout', employee_logout , name='employee_logout'),

    path('profile',profile,name = 'profile'),
   

]