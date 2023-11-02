from django.db import models
from django.utils.html import mark_safe
from datetime import date
from colorfield.fields import ColorField

# Create your models here.

class Section(models.Model):
    SECTIONS = [
        ('offer', 'Angebot'),
        ('about', 'About'),
    ]
    section = models.CharField(max_length=5, choices=SECTIONS, default='offer')
    title = models.CharField(max_length= 50)
    text = models.TextField()

    def __str__(self):
        return  self.title

class BlogTag(models.Model):
    name = models.CharField(max_length=40)
    color = ColorField()
    text_color = ColorField(default = '#000')

    def __str__(self):
        return  self.name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    published = models.BooleanField(default=True)
    tag = models.ForeignKey(BlogTag, on_delete=models.PROTECT) 
    text = models.TextField()  
    date = models.DateField(default= date.today)
    img = models.ImageField(upload_to='uploads/blogimages')
    img_alt = models.CharField(max_length=40)

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.img.url}" width = "200"/>')
    
    def __str__(self):
        return  self.title 
    
    class Meta:
        ordering = ('-date',)

class BlogImage(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='uploads/blogimages')  
    img_alt = models.CharField(max_length=40) 
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.img.url}" width = "200"/>')
    
    def __str__(self):
        return  self.name

class Testimonials(models.Model):
    name = models.CharField(max_length=60)
    published = models.BooleanField(default=True)
    text = models.TextField()
    date = models.DateField(default=date.today)

class GalleryImage(models.Model):
    img = models.ImageField(upload_to='uploads/gallery')
    img_alt = models.CharField(max_length=40)
    subtitle = models.TextField()  

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.img.url}" width = "200"/>')
    
    def __str__(self):
        return  self.subtitle

class Partner(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='uploads/partners')
    img_alt = models.CharField(max_length=40)
    link = models.URLField()     

class Offers(models.Model):
    title = models.CharField(max_length=40)
    short_text = models.TextField()
    icon = models.ImageField(upload_to='uploads/icons')     
