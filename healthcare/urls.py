
from django.urls import path
from healthcare import views


urlpatterns = [
   path("",views.home,name="home"),
   path("Doctors",views.doctor,name="doctor"),

   path('Services', views.services, name='services'), 
   path('Services/<slug:slug>/', views.display_slug, name='slug'),  
   path("About",views.about,name="about"),
   path("Contact",views.contact,name="contact"),
   path('Appointment',views.appointment,name="appointment"),
   path('Departments',views.department,name="department"),

]

