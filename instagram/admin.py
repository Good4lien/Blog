from django.contrib import admin
from .models import Posts


class PostsAdmin(admin.ModelAdmin):
    fields = (('photo_preview', 'photo_load'), 'text', ('views', 'likes'), 'tags', 'date')
    list_display = ('photo_preview', 'text', 'views', 'likes', 'tags', 'date')
    readonly_fields = ['photo_preview']

admin.site.register(Posts, PostsAdmin)