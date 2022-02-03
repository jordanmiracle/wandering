from django.db import models


class SlideShow(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='')
    title = models.TextField(blank=True, null=True)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.description
