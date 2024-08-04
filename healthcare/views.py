from django.shortcuts import render

from .models import *
def home(request):
    data={
        'bannerData': Banner.objects.all(),
    }
    
    return render(request,'pages/home/home.html',data)


def about(request):
    
    return render(request,'pages/about/about.html',)


def appointment(request):
    
    return render(request,'pages/appointment/appointment.html',)

def contact(request):
    
    return render(request,'pages/contact/contact.html',)

def services(request):
    
    return render(request,'pages/our_services/services.html',)


def doctor(request):
    
    return render(request,'pages/doctor/doctor.html',)
