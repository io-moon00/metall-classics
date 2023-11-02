from django.contrib import admin
from .models import Blog, BlogImage, BlogTag, GalleryImage, Partner, Offers, Testimonials, Section

# Register your models here.

class GalleryImageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['__str__', 'img_preview']

class BlogImgAdmin(admin.StackedInline):
    list_display = ['__str__', 'img_preview']
    readonly_fields = ['img_preview']
    model = BlogImage

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    inlines = [BlogImgAdmin]

    class Meta:
        model = Blog

@admin.register(BlogImage)
class BlogImgAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogTag)
admin.site.register(GalleryImage, GalleryImageAdmin)
