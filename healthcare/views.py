from django.shortcuts import render

from healthcare.models import *

def home(request):
    banner = Category.objects.get(name='gallery')
    data={
        'bannerData':Hospital.objects.filter(category =banner)[:4],
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
