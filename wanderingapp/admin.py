from django.contrib import admin
from django.utils.html import format_html
from .models import Slider, SliderImage


class SliderImageAdmin(admin.TabularInline):
    model = SliderImage
    readonly_fields = ('image_preview',)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    inlines = [SliderImageAdmin]

    class Meta:
        model = Slider

    def __str__(self):
        return self.title


@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):

    def __str__(self):
        return self.title
