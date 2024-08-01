
from django.urls import path
from healthcare import views


urlpatterns = [
   path("",views.home,name="home"),
   path("About",views.about,name="about"),
   path("Contact",views.contact,name="contact"),
   

]

