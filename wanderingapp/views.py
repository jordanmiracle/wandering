from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from wanderingapp.forms import ContactForm
#from wanderingproject.devsettings import EMAIL_HOST_USER
#from wanderingproject.devsettings import AUTH_USER
from .models import Slider, SliderImage
from .forms import ContactForm
from wanderingproject import settings
from wanderingproject.settings import EMAIL_HOST_USER
from django.conf import settings
#from wanderingproject import devsettings
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from wanderingproject import settings

def blog_view(request):
    posts = Slider.objects.all()
    return render(request, 'wanderingapp/index.html', {'posts': posts})


# ef contact(request):
#   if request.method == 'POST':
#       form = ContactForm(request.POST or None)
#       if form.is_valid():
#           name = request.POST.get('name')
#           subject = request.POST.get('subject')
#           email = request.POST.get('email')
#           message = request.POST.get('message')
#           context = {
#               'form': form,
#           }
#           return context

#   form = ContactForm()
#   return render(request, 'wanderingapp/index.html', {'form': form})

def index(request):
    post = get_object_or_404(Slider)
    photos = SliderImage.objects.filter()
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # assert false
            con = get_connection('django.core.mail.backends.smtp.EmailBackend')
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                recipient_list=('ellen@mtbakerweddings.com',),
                connection=con
            )
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'wanderingapp/index.html', {
        'post': post,
        'photos': photos,
        'form': form,
        'submitted': submitted
    })


def coming_soon(request):
    return render(request, 'wanderingapp/coming_soon.html')
