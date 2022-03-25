from django.db import models


class Post(models.Model):
    image = models.FileField(blank=True)


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='')
