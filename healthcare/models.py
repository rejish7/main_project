from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField( max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
class Banner(models.Model):
    image1 = models.ImageField(upload_to='banner')
    title1 = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    
class Setting(models.Model):
    name = models.CharField( max_length=50,unique=True)
    logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    address = models.CharField( max_length=100,null=True,blank=True)
    phone = models.CharField( max_length=100,null=True,blank=True)
    email = models.CharField( max_length=100,null=True,blank=True)
    facebook = models.CharField( max_length=100,null=True,blank=True)
    twitter = models.CharField( max_length=100,null=True,blank=True)
    instagram = models.CharField( max_length=100,null=True,blank=True)
    linkedin = models.CharField( max_length=100,null=True,blank=True)
    youtube = models.CharField( max_length=100,null=True,blank=True)
    about = RichTextField()
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Setting'




class Schedule(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'

class OpeningHours(models.Model):
    day = models.CharField(max_length=20)
    hours = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.day}: {self.hours}"

    class Meta:
        verbose_name = 'Opening Hour'
        verbose_name_plural = 'Opening Hours'

class FunFact(models.Model):
    icon = models.CharField(max_length=50)
    count = models.IntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Fun Fact'
        verbose_name_plural = 'Fun Facts'

class CallToAction(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    button1_text = models.CharField(max_length=50)
    button1_link = models.URLField()
    button2_text = models.CharField(max_length=50)
    button2_link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Call to Action'
        verbose_name_plural = 'Call to Actions'

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.department}"

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.doctor} - {self.appointment_date}"

    class Meta:
        permissions = [
            ("view_appointment", "Can view appointment"),
            ("change_appointment", "Can change appointment"),
        ]
    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class DoctorPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Doctor Page'
        verbose_name_plural = 'Doctor Pages'
        
class OverviewSetting(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField()
    image = models.ImageField(upload_to='overview_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Overview Setting'
        verbose_name_plural = 'Overview Settings'

class OverviewSection(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='overview_images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Overview Section'
        verbose_name_plural = 'Overview Sections'

class EmergencyService(models.Model):
    title = models.CharField(max_length=200, default="Emergency Services")
    description = models.TextField()
    image = models.ImageField(upload_to='emergency_services/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Emergency Service'
        verbose_name_plural = 'Emergency Services'

class EmergencyContact(models.Model):
    phone_number = models.CharField(max_length=20)
    emergency_service = models.ForeignKey(EmergencyService, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.phone_number

class ServiceDetail(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='service_details/', null=True, blank=True)
    learn_more_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service Detail'
        verbose_name_plural = 'Service Details'
