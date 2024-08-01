
from django.contrib import admin
from .models import *
from django.db.models import Count

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
  list_display = ['name','email','phone']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display =['name','slug']
  prepopulated_fields = {'slug': ('name',)}


@admin.register(Hospital)
class NewsAdmin(admin.ModelAdmin):
  list_display = ['category']
  list_display = ['title','category','status','updated_at','image']
  prepopulated_fields = {'slug':('title',)}