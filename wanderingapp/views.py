from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from wanderingapp.forms import ContactForm
from .models import Slider, SliderImage
from .forms import ContactForm
from wanderingproject import settings
from django.conf import settings

def blog_view(request):
    posts = Slider.objects.all()
    return render(request, 'wanderingapp/index.html', {'posts': posts})


def index(request):
    post = get_object_or_404(Slider)
    photos = SliderImage.objects.filter()
    form_class = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = request.POST.get('name')
            subject = request.POST.get('subject')
            email = request.POST.get('email')
            message = request.POST.get('message')

            send_mail('{}'.format(subject), '{}'.format(message), '{}'.format(email), [settings.EMAIL_HOST_USER],
                      fail_silently=False)
            return HttpResponseRedirect(ContactForm)
    return render(request, 'wanderingapp/index.html', {
        'post': post,
        'photos': photos,
        'form': form_class})


def coming_soon(request):
    return render(request, 'wanderingapp/coming_soon.html')