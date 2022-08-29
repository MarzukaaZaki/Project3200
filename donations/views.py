from django.shortcuts import render
from donations.models import EligibilityQuiz
from django.core.mail import send_mail
# Create your views here.
def eligibilityQuiz(request):
    if request.method == 'POST':
        print(request.POST)
        questions = EligibilityQuiz.objects.all()
        score = 0
        total = 0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
        percent= (score/(total*10))*100
        print(percent,"%")
        context = {
            'total':total,
            'score':score,
            'percent':percent,
            }

        return render(request,'result.html',context)
    else:
        questions=EligibilityQuiz.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'eligibility_quiz.html',context)
        
def appointment(request):
    if request.method=="POST":
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        date_of_appointment=request.POST['date']

        send_mail(
            first_name+last_name, # Subject
            'I would like to book an appointment on '+date_of_appointment, # Body of email
            email, # Sender
            ['zakimarzuka@gmail.com'] # Receipient
            )
        return render(request, 'appointment.html',{'first_name':first_name})
    else:
        return render(request, 'appointment.html',{})

def blood_request(request):
    if request.method=="POST":
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        blood_group = request.POST['bloodgroup']
        quantity = request.POST['quantity']
        date_of_appointment=request.POST['date']

        send_mail(
            first_name+last_name, # Subject
            'I need '+ quantity + ' of ' + blood_group+' blood within '+date_of_appointment, # Body of email
            email, # Sender
            ['zakimarzuka@gmail.com'] # Receipient
            )
        return render(request, 'blood_request.html',{'first_name':first_name})
    else:
        return render(request, 'blood_request.html',{})

 
