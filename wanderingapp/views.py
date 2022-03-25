from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, PostImage


def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def index(request):
    post = get_object_or_404(Post)
    photos = PostImage.objects.filter()
    return render(request, 'wanderingapp/index.html', {
        'post': post,
        'photos': photos
    })


def addPhoto(request):
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        for image in images:
            photo = PostImage.objects.create(
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    return render(request, 'photos/add.html')
