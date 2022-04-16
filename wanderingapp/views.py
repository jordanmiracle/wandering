from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .models import Slider, SliderImage


def blog_view(request):
    posts = Slider.objects.all()
    return render(request, 'wanderingapp/index.html', {'posts': posts})


def index(request):
    post = get_object_or_404(Slider)
    photos = SliderImage.objects.filter()
    return render(request, 'wanderingapp/index.html', {
        'post': post,
        'photos': photos
    })


def addPhoto(request):
    for image in SliderImage:
        photo = SliderImage.objects.create(
            image=image,
        )

        return redirect('gallery')

    return render(request, 'wanderingapp/add_photo.html', {})
