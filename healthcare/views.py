from django.shortcuts import render ,redirect
from django.contrib import messages
import os
from django.urls import reverse

from .models import *



def home(request):
    banners = Banner.objects.all()
    schedule = Schedule.objects.all()
    funfact = FunFact.objects.all()
    data = {
        'banners': banners,
        'schedules':schedule,
        'funfacts':funfact
    }
    return render(request, 'pages/home/home.html', data)
def about(request):
    
    return render(request,'pages/about/about.html',)


def appointment(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        department_id = request.POST.get('department')
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        reason = request.POST.get('reason')

        doctor = Doctor.objects.get(id=doctor_id)
        department = Department.objects.get(id=department_id)

        Appointment.objects.create(
            patient_name=patient_name,
            department=department,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            reason=reason
        )
        messages.success(request, 'Appointment booked successfully')
        return redirect("/")   
    else:
        data = {
            'appointments': Appointment.objects.all(),
            'departments': Department.objects.all(),
            'doctors': Doctor.objects.all(),
        }
    return render(request, 'pages/appointment/appointment.html', data)

def contact(request):
    
    return render(request,'pages/contact/contact.html',)

def services(request):
    data = {
        'serviceData': ServiceDetail.objects.all(),
    }

    return render(request, 'pages/our_services/services.html', data)

def display_slug(request, slug):
    service = ServiceDetail.objects.get(slug=slug)
    data = {
        'service': service,
    }
    return render(request, 'pages/our_services/service_detail.html', data)


def doctor(request):
    
    doctor = Doctor.objects.all()
    data={
        'doctors': doctor,
    }
    return render(request,'pages/doctor/doctor.html',data)

def department(request):
    data={
    'departments': Department.objects.all(),}
    return render(request,'pages/department/department.html',data)