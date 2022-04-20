from django.db import models
from django.utils.safestring import mark_safe


class Slider(models.Model):
    image = models.FileField(blank=True)


class SliderImage(models.Model):
    slider = models.ForeignKey(Slider, default=None, on_delete=models.CASCADE)
    title = models.CharField(blank=True, null=True, max_length=250, default='')
    images = models.FileField(upload_to='')
