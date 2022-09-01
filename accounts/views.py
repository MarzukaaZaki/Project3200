from django.views.generic import TemplateView, CreateView, View
from accounts.forms import (
    DonorLoginForm, DonorSignUpForm, 
    PatientSignUpForm, PatientLoginForm, 
    EmployeeSignUpForm, EmployeeLoginForm,
    UserUpdateForm, ProfileUpdateForm
    )
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
class RegisterView(TemplateView):
    template_name = 'register.html'


class DonorRegisterView(CreateView):
    form_class = DonorSignUpForm
    template_name = 'donor_register.html'
    success_url = '/home'


class DonorLoginView(View):
    template_name = 'donor_login.html'
    form_class = DonorLoginForm
    def get(self, request):
        form = self.form_class()
        message =''
        return render(request, self.template_name, context = {'form':form,'message':message})
    
    def post(self, request):
        form = self.form_class(request.POST)
        message =''
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect("/home")
        else:
            return render(request, self.template_name, context = {'form':form,'message':message})



def donor_logout(request):
    logout(request)
    return redirect("donor_login")



class PatientRegisterView(CreateView):
    form_class = PatientSignUpForm
    template_name = 'patient_register.html'
    success_url = '/home'



class PatientLoginView(View):
    template_name = 'patient_login.html'
    form_class = PatientLoginForm
    def get(self, request):
        form = self.form_class()
        message =''
        return render(request, self.template_name, context = {'form':form,'message':message})
    
    def post(self, request):
        form = self.form_class(request.POST)
        message =''
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect("/home")
        else:
            return render(request, self.template_name, context = {'form':form,'message':message})




def patient_logout(request):
    logout(request)
    return redirect("patient_login")




class EmployeeRegisterView(CreateView):
    form_class = EmployeeSignUpForm
    template_name = 'employee_register.html'
    success_url = '/home'



class EmployeeLoginView(View):
    template_name = 'employee_login.html'
    form_class = EmployeeLoginForm
    def get(self, request):
        form = self.form_class()
        message =''
        return render(request, self.template_name, context = {'form':form,'message':message})
    
    def post(self, request):
        form = self.form_class(request.POST)
        message =''
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect("/home")
        else:
            return render(request, self.template_name, context = {'form':form,'message':message})



def employee_logout(request):
    logout(request)
    return redirect("employee_login")


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
        request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Profile Updated Successfully!')
            return redirect('profile')
    else:
         u_form = UserUpdateForm(instance=request.user)
         p_form = ProfileUpdateForm(instance=request.user.profile)
        


    
    context = {'u_form':u_form, 'p_form':p_form}
    return render(request,'profile.html', context)
