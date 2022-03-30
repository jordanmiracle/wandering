from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .models import Post, PostImage


def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'wanderingapp/index.html', {'posts': posts})


def index(request):
    post = get_object_or_404(Post)
    photos = PostImage.objects.filter()
    return render(request, 'wanderingapp/index.html', {
        'post': post,
        'photos': photos
    })


def addPhoto(request):
    for image in PostImage:
        photo = PostImage.objects.create(
            image=image,
        )

        return redirect('gallery')

    return render(request, 'wanderingapp/add_photo.html', {})
