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

class Testimonial(models.Model):
    name = models.CharField(max_length=60)
    published = models.BooleanField(default=True)
    text = models.TextField()
    date = models.DateField(default=date.today)

class GalleryImage(models.Model):
    img = models.ImageField(upload_to='uploads/gallery')
    img_alt = models.CharField(max_length=40)
    subtitle = models.TextField(blank=True)  

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.img.url}" width = "200"/>')
    
    def __str__(self):
        return  self.img_alt

class Partner(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='uploads/partners')
    img_alt = models.CharField(max_length=40)
    link = models.URLField()     
    text_color = ColorField(default = 'rgb(38, 134, 146)')
    bg_color = ColorField(default = 'rgb(243, 243, 243)')

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.logo.url}" width = "200"/>')
    
    def __str__(self):
        return  self.name

class Offer(models.Model):
    title = models.CharField(max_length=40)
    short_text = models.TextField()
    icon = models.ImageField(upload_to='uploads/icons')     

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.icon.url}" width = "200"/>')
    
    def __str__(self):
        return  self.title
    
PAGES = [
        ('home', 'Home'),
        ('gallery', 'Gallerie'),
        ('blog', 'Blog'),
        ('impressum', 'Impressum'),
        ('dataprotection', 'Datenschutzerklärung'),
    ]

POSITIONS_VERT = [
    ('center', 'Center'),
    ('top', 'Top'),
    ('bottom', 'Bottom'),
]

POSITIONS_HORI = [
    ('center', 'Center'),
    ('left', 'Left'),
    ('right', 'Right'),
]

class Page(models.Model):
    title = models.CharField(max_length=120)
    page = models.CharField(max_length=14, choices=PAGES) 
    text = models.TextField()   
    hero = models.ImageField(upload_to='uploads')
    hero_alt = models.CharField(max_length= 50)
    vert_position = models.CharField(max_length=6, choices=POSITIONS_VERT, default='center')
    hori_position = models.CharField(max_length=6, choices=POSITIONS_HORI, default='center')

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.hero.url}" width = "200"/>')
    
    def __str__(self):
      return self.page