from django.shortcuts import render ,redirect
from django.contrib import messages

from .models import *
def home(request):
    data={
        'bannerData': Banner.objects.all(),
    }
    
    return render(request,'pages/home/home.html',data)


def about(request):
    
    return render(request,'pages/about/about.html',)


def appointment(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        reason = request.POST.get('reason')

        doctor = Doctor.objects.get(id=doctor_id)

        appointment = Appointment.objects.create(
            patient_name=patient_name,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            reason=reason
        )
        messages.success(request,'Data inserted successfully')
        return redirect(request, 'pages/appointment/appointment.html')
    else:
        data={'appointmentdata':Appointment.objects.all()}
    return render(request, 'pages/appointment/appointment.html', data)

def contact(request):
    
    return render(request,'pages/contact/contact.html',)

def services(request):
    
    return render(request,'pages/our_services/services.html',)


def doctor(request):
    
    return render(request,'pages/doctor/doctor.html',)

def overview(request):
    
    return render(request,'pages/overview/overview.html',)