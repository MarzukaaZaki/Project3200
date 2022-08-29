from django.urls import path
from .views import blood_request, eligibilityQuiz, appointment
urlpatterns = [
    path('eligibility_quiz/',eligibilityQuiz, name ='eligibility_quiz'),
    path('appointment',appointment, name='appointment'),
    path('blood_request', blood_request,name='blood_request')
    
]