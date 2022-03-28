from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from wanderingapp import views

app_name = 'wanderingapp'

urlpatterns = [
    path("add/", views.addPhoto, name="addPhoto")

]
