from django.shortcuts import render

from .models import Slideshow


def index(request):
    photos = Slideshow.objects.all()
    context = {
        'photos': photos
    }
    return render(request, 'wanderingapp/index.html', context)

# def addPhoto(request):
#    if request.method == 'POST':
#        data = request.POST
#        images = request.FILES.getlist('images')
