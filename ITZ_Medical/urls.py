"""ITZ_Medical URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path,include
from App import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # frontend
    path('', views.frontend,name='frontend'),
    # doctor backend
    path('medical/backend', views.staff_backend,name='backend'),
    path('doctor_detail',views.doctor_detail, name='doctor_detail'),
    # patient backend
    path('medical/backend/patient', views.patient_backend,name='patient_backend'),
    path('patient-dashboard/patient-report/generate',views.patient_report, name='patient_report'),
    # nurse backend
    path("medical/backend/nurse", views.nurse_backend, name="nurse_backend"),
    # nursing assistant backend
    path("medical/backend/nursing_assistant", views.nursing_assistant_backend, name="nursing_assistant_backend"),
    
    
    
    
    # detail pages for doctors
    path('doctor_dashboard/all_patients/',views.all_patients, name='all_patients'),
    path('doctor_dashboard/recent_patients/',views.recent_patients, name='recent_patients'),
    path('doctor_dashboard/recovered_patients/',views.recovered_patients, name='recovered_patients'),
    path('doctor_dashboard/pending_patients/',views.pending_patients, name='pending_patients'),
    path('doctor_dashboard/appoitments/',views.patients_appoitment, name='patient_appoitment'),
    path('doctor_dashboard/all_reviews/',views.all_reviews, name='all_reviews'),
    path('doctor_dashboard/my_clinic/',views.my_clinic, name='my_clinic'),
    

    
    # auth PATHS
    
    path('login/', views.login_handle,name='login'),
    path('logout/', views.logout_handle,name='logout'),
    path('patient_register/',views.patient_register.as_view(), name='patient_register'),
    path('doctor_register/',views.doctor_register.as_view(), name='doctor_register'),
    path('nurse_register/',views.nurse_register.as_view(), name='nurse_register'),
    path('nursing_assistant_register/',views.nursing_assistant_register.as_view(), name='nursing_assistant_register'),
    path('change_password/doctor',views.change_password_doctor, name='change_password_doctor'),
    path('change_password/patient',views.change_password_patient, name='change_password_patient'),
    path('change_password/nurse',views.change_password_nurse, name='change_password_nurse'),
    path('doctor_dashboard/auth/update_profile/', views.update_profile,name='update_profile'),
    path('patient_dashboard/auth/update_profile/', views.patient_update_profile,name='patient_update_profile'),

    
    
    #  reset password
    path('reset_password/',auth_views.PasswordResetView.as_view(),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(), 
        name="password_reset_complete"),


    
    #pharmacy views
    path('', include('pharmacy.urls')),


    
    
    
    
    # test Url
    
    path('test/', views.test,name='test'),
    path('pharmacy/cart/', views.cart,name='cart'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()





