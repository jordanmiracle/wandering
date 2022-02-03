from django.shortcuts import render


def index(request):
    return render(request, 'wanderingapp/index.html', {})


def addPhoto(request):
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
