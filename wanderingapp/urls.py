from rest_framework import routers
from django.urls import path, include
from wanderingapp import views

router = routers.DefaultRouter()
router.register(r'vue_index', views.index)

urlpatterns = [
    path('', include(router.urls))
]
