from django.contrib import admin
from django.utils.html import format_html
from .models import Slider, SliderImage
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin, SortableGenericInlineAdminMixin, \
    SortableAdminBase


# @admin.register(SliderImage)
# class SortableSliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
#    pass


class SliderImageAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = SliderImage
    readonly_fields = ('image_preview',)
    ordering = ['image_order']


@admin.register(Slider)
class SliderAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [SliderImageAdmin]
    ordering = ['image_order']

    class Meta:
        model = Slider

    def __str__(self):
        return self.title


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = ['image_order']

    def __str__(self):
        return self.title


admin.site.site_header = 'Wandering Waters Dashboard'
