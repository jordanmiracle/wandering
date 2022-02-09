from django.db import models


class Slideshow(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='')
    title = models.TextField(blank=True, null=True, max_length=150)
    description = models.TextField(null=False, blank=False, max_length=500)

    def __str__(self):
        return self.title
