from django.contrib import admin
from .models import Blog, BlogImage, BlogTag, GalleryImage, Partner, Offer, Testimonial, Section, Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['__str__','title', 'img_preview']

class GalleryImageAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['__str__', 'img_preview']

class OffersAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    list_display = ['__str__', 'img_preview']

class PartnerAdmin(admin.ModelAdmin):
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
admin.site.register(Offer, OffersAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Testimonial)
admin.site.register(Section)
admin.site.register(Page, PageAdmin)
