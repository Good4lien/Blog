from django.contrib import admin
from .models import Posts, Tags, Messages, Follow


class PostsAdmin(admin.ModelAdmin):
    empty_value_display = ''
    ordering = ['-date']
    list_max_show_all = 10
    list_filter = ('category', 'tags')
    fields = ('moderation', 'category', ('image_preview', 'image_load'), 'title', 'preview', 'content', 'tags', ('date', 'hold', 'likes'))
    search_fields = ['title']
    readonly_fields = ['image_preview']
    list_display = ('moderation', 'image_preview', 'title', 'preview', 'category', 'likes', 'date', 'hold', 'edit')
    list_display_links =('title', 'edit')
    list_per_page = 10
    save_as = True
    save_on_top = True
    actions_on_top = False

    def view_on_site(self, obj):
        return '/post/{0}'.format(obj.id)


admin.site.register(Posts, PostsAdmin)
admin.site.register(Tags)
admin.site.register(Messages)
admin.site.register(Follow)

