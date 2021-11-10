from django.db import models
from ckeditor.fields import RichTextField, RichTextFormField
from ckeditor.widgets import CKEditorWidget


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
