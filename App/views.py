from urllib import request

from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import *
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth.forms import *
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from .models import *





# Create your views here.
def frontend(request):
 return render(request,'index.html')


@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def staff_backend(request):
    if request.user.is_doctor:
        return render(request,'dashboard/index.html')
    else:
        return render (request,'404.html')
    
    

# patient backend
@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def patient_backend(request):
    if request.user.is_patient:
        return render(request,'patient_dashboard/index.html')
    else:
        return render (request,'404.html')
    
        
    
    
# nurse backend
@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def nurse_backend(request):
    if request.user.is_nurse:
        return render(request,'nurse_dashboard/index.html')
    else:
        return render(request,'404.html')
        

# nurse backend
@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def nursing_assistant_backend(request):
    if request.user.is_nursing_assistant:
        return render(request,'nursing_assistant/index.html')
    else:
        return render(request,'404.html')
        


# For auth 
def login_handle(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password,)
           


        if user is not None:
            login(request,user)
            messages.success(request,'success')
            if request.user.is_doctor:
                return redirect('backend')
            elif request.user.is_nurse:
                return redirect('nurse_backend')
            elif request.user.is_patient:
                return redirect('patient_backend')
            else:
                return redirect('nursing_assistant_backend')
                   
                    
            
        else:
            messages.error(request,'error')    
            return redirect('login')    

      
    return render(request,'registration/login.html')

@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def logout_handle(request):
 logout(request)
 return redirect('login')



# changes passwords

@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def change_password_doctor(request):
    if request.method == "POST":
        fm=PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'success')
            return redirect('change_password_doctor')

    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request,'registration/change_password_doctor.html',{'form': fm})


@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def change_password_patient(request):
    if request.method == "POST":
        fm=PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            messages.success(request,'success')
            fm.save()
            
            return redirect('change_password_patient')

    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request,'registration/change_password_patient.html',{'form': fm})


@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def change_password_nurse(request):
    if request.method == "POST":
        fm=PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            messages.success(request,'success')
            fm.save()
            
            return redirect('change_password_nurse')

    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request,'registration/change_password_nurse.html',{'form': fm})



# signup method cheat




class patient_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('patient_backend')

class doctor_register(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('backend')


class nurse_register(CreateView):
    model = User
    form_class = NurseSignUpForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('nurse_backend')


class nursing_assistant_register(CreateView):
    model = User
    form_class = NursingAssistantSignUpForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('nursing_assistant_backend')







@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def doctor_detail(request):
    if request.method == "POST":
        fm=doctorform( data=request.POST)
        if fm.is_valid():
            ins = fm.save()
            messages.success(request,'success')
            return render(request,'dashboard/doctor/doctor_detail.html',{'form':doctorform(instance=ins)})

    else:
        fm=doctorform()
        

    return render(request,'dashboard/doctor/doctor_detail.html',{'form': fm})















@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def update_profile(request):
    if request.user.is_doctor:
    
        return render(request,'registration/update-profile.html')



# patient-report
@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def patient_report(request):
    if request.user.is_patient:
        return render(request,'patient_dashboard/report.html')



@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def patient_update_profile(request):
    if request.user.is_patient:
    
        return render(request,'patient_dashboard/update_profile.html')




# detail pages for doctor
@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def all_patients(request):
    if request.user.is_doctor:
        return render(request,'dashboard/doctor/patient_list/all_patients.html')

@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def recent_patients(request):
    if request.user.is_doctor:
        return render(request,'dashboard/doctor/patient_list/recent_patients.html')


@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def recovered_patients(request):
    if request.user.is_doctor:
        return render(request,'dashboard/doctor/patient_list/recovered_patients.html')


@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def pending_patients(request):
    if request.user.is_doctor:
        return render(request,'dashboard/doctor/patient_list/pending_patients.html')


@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def patients_appoitment(request):
    if request.user.is_doctor:
        return render(request,'dashboard/doctor/patient_list/appoitment.html')


@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def all_reviews(request):
    if request.user.is_doctor:
        return render(request,'dashboard/doctor/all_reviews.html')
@cache_control(no_cache=True, must_revalidate=True , no_store=True)
@login_required(login_url='login')
def my_clinic(request):
    if request.user.is_doctor:
        return render(request,'dashboard/inbox.html')






# test view

def test(request):
    return render(request,'dashboard/inbox.html')