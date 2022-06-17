from django.urls import reverse_lazy

from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from importlib_metadata import files
from .models import *

class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    gender = forms.ChoiceField(choices= GENDER_CHOICES)


    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.gender = self.cleaned_data.get('gender')
        
        user.save()
        return user

class DoctorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    gender = forms.ChoiceField(choices= GENDER_CHOICES)


    

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        
        user.gender = self.cleaned_data.get('gender')

        user.save()
        return user


class NurseSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    gender = forms.ChoiceField(choices= GENDER_CHOICES)
    

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_nurse = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.gender = self.cleaned_data.get('gender')
        user.save()
        return user


class NursingAssistantSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    gender = forms.ChoiceField(choices= GENDER_CHOICES)
    

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_nursing_assistant = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.gender = self.cleaned_data.get('gender')
        user.save()
        return user
    





class DateInput(forms.DateInput):
        input_type = 'date'
    
class doctorform(forms.ModelForm):
    dob=forms.DateField(widget=DateInput)
    class Meta:
        model = Doctor
        fields = '__all__'
            
