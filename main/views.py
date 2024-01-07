from datetime import date
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from forms.forms import ContactForm
from django. conf import settings
from .models import Blog, BlogImage, GalleryImage, Offer, Page
# Create your views here.
current_year = date.today().year

def home(request):
    blogs = Blog.objects.filter(published = True)[:3]
    offers = Offer.objects.all()
    page = Page.objects.get(page = 'home')
    images = GalleryImage.objects.all()[:4]
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject, from_email, to = 'Metall Classics Kontaktformular', settings.EMAIL_HOST_USER, 'craft@metall-classics.ch'
            html_content = render_to_string('email.html', {'salutation':cd['salutation'], 'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'message':cd['message']})
            text_content = render_to_string('email.txt', {'salutation':cd['salutation'], 'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'message':cd['message']})
                
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect('?submitted=True#contact')


    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'home.html',{'form': form, 
                                        'year': current_year, 
                                        'submitted': submitted, 
                                        'page': page,
                                        'blogs': blogs, 
                                        'images': images,
                                        'offers': offers})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    images = BlogImage.objects.filter(blog=blog)

    return render(request, 'blog-detail-view.html', {'year': current_year, 'blog': blog, 'images': images})


def blog(request):
    blogs = Blog.objects.filter(published = True)
    page = Page.objects.get(page='blog')
    return render(request, 'blog.html', {'year': current_year, 'page':page, 'blogs': blogs})

def gallery(request):
    images = GalleryImage.objects.all()
    page = Page.objects.get(page='gallery')

    return render(request, 'gallery.html', {'year': current_year, 'page':page, 'images': images})

def impressum(request):
    page = Page.objects.get(page='impressum')
    return render(request, 'impressum.html', {'year': current_year, 'page':page})

def legal(request):
    page = Page.objects.get(page='dataprotection')
    return render(request, 'legal.html', {'year': current_year, 'page':page})