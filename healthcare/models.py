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
    


class Hospital(models.Model):
    created_at =  models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey( Category,on_delete=models.CASCADE)
    title = models.CharField( max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    image = models.ImageField(upload_to='image',null=True,blank=True)
    description = RichTextField()
    meta_description = models.CharField( max_length=100,null=True,blank=True)
    meta_keyword = models.CharField( max_length=100,null=True,blank=True)
    status = models.BooleanField(default=True,blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospital'
        
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
    

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Setting'
