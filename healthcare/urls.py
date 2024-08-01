
from django.urls import path
from healthcare import views


urlpatterns = [
   path("",views.home,name="home"),
]

