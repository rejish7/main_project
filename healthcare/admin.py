
from django.contrib import admin
from .models import *
from django.db.models import Count
from django.utils.html import format_html


from django.contrib import admin
from .models import *

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
  list_display = ['name', 'email', 'phone']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = {'slug': ('name',)}

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
  list_display = ['title1', 'show_image']
  readonly_fields = ['show_image']

  def show_image(self, obj):
      if obj.image1:
          return format_html('<img src="{}" width="100" height="auto" />', obj.image1.url)
      return ''

  show_image.short_description = 'Image Preview'
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
  list_display = ['title', 'icon', 'link']

@admin.register(OpeningHours)
class OpeningHoursAdmin(admin.ModelAdmin):
  list_display = ['day', 'hours']

@admin.register(FunFact)
class FunFactAdmin(admin.ModelAdmin):
  list_display = ['icon', 'count', 'description']

@admin.register(CallToAction)
class CallToActionAdmin(admin.ModelAdmin):
  list_display = ['title', 'phone_number']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
  list_display = ['name']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
  list_display = ['name', 'department']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
  list_display = ['patient_name', 'doctor', 'appointment_date', 'appointment_time', 'reason', 'created_at']
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
  list_display = ['title', 'slug']
  prepopulated_fields = {'slug': ('title',)}

@admin.register(DoctorPage)
class DoctorPageAdmin(admin.ModelAdmin):
  list_display = ['name','content']

@admin.register(OverviewSetting)
class OverviewSettingAdmin(admin.ModelAdmin):
  list_display = ['name']

@admin.register(OverviewSection)
class OverviewSectionAdmin(admin.ModelAdmin):
  list_display = ['title']


@admin.register(ServiceDetail)
class ServiceDetailAdmin(admin.ModelAdmin):
  list_display = ['title','image','learn_more_link']