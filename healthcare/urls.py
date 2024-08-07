
from django.urls import path
from healthcare import views


urlpatterns = [
   path("",views.home,name="home"),
   path("Overview",views.overview,name="overview"),
   path("Services",views.services,name="services"),
   path("About",views.about,name="about"),
   path("Contact",views.contact,name="contact"),
   path('Appointment',views.appointment,name="appointment"),
   path('Find a Doctor',views.doctor,name="doctor"),

]

