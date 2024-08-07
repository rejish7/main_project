from django.shortcuts import render ,redirect
from django.contrib import messages
import os

from .models import *
def home(request):
    banners = Banner.objects.all()
   
    data = {
        'banners': banners,
    }
    return render(request, 'pages/home/home.html', data)

def deletepath(id):
    obj1 = Banner.objects.get(id=id)
    if obj1.image1:
        if os.path.exists(obj1.image1.path):
            os.remove(obj1.image1.path)
        return True
    else:
        return True

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
    
    return render(request,'pages/our_services/services.html',)


def doctor(request):
    data={
    'departments': Department.objects.all(),}
    
    return render(request,'pages/doctor/doctor.html',data)

def overview(request):
    
    return render(request,'pages/overview/overview.html',)