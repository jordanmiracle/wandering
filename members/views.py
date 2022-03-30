from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from wanderingapp.models import PostImage
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, "There Was An Error Logging In, Try Again...")
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})
