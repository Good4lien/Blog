from django.contrib import admin
from .models import Books


class ReadingAdmin(admin.ModelAdmin):
    empty_value_display = ''
    fields = ('hold', ('image_preview', 'image_load'), 'title', 'author', 'html', 'css')
    readonly_fields = ['image_preview']
    list_display = ('image_preview', 'title', 'author', 'hold')
    list_display_links =('title', 'image_preview')

# Register your models here.
admin.site.register(Books, ReadingAdmin)