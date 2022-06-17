
from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from datetime import date




GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    is_nursing_assistant = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email= models.EmailField(max_length=254)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES ,)

    
    
class Doctor(models.Model):
    first_name = models.CharField( max_length=50)
    father_name = models.CharField (max_length=50)
    mother_name = models.CharField (max_length=50)
    dob = models.DateField()
    age = models.IntegerField() 
    contact_no = models.IntegerField()
    mobile_no = models.IntegerField()
    city = models.CharField (max_length=50)
    province = models.CharField (max_length=50)
    country = models.CharField (max_length=50)
    address = models.CharField (max_length=100)
    profile_pic = models.ImageField(upload_to=None,null=True ,blank=True)
    doctor_reg_No = models.CharField (max_length=50)
    universty = models.CharField (max_length=50)
    specialty = models.CharField (max_length=50)
    job_experiance = models.CharField (max_length=50)
    last_hospital = models.CharField (max_length=50)
    pay_demand = models.IntegerField()
    cv = models.FileField (upload_to=None, max_length=100 ,null=True ,blank=True)
    
    def __str__(self):
        return self.first_name
    
    
        
    

    

    


