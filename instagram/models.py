from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.safestring import mark_safe


class Posts(models.Model):
    class Meta():
        verbose_name='Post'
        verbose_name_plural='Posts'

    photo_load = models.ImageField(null=True, blank=True, upload_to = 'media/instagram/images/', verbose_name='', max_length=256)
    photo = ImageSpecField(source='photo_load', processors=[ResizeToFill(1000, 1000)], format='JPEG', options={'quality': 100})
    text = models.TextField(max_length=3000, blank=True, null=True, default='')
    tags = models.CharField("Tags", max_length=1000, blank=True, null=True, default='')
    likes = models.IntegerField(default=0, verbose_name='Likes', blank=True)
    views = models.IntegerField(default=0, verbose_name='Views', blank=True)
    date = models.DateField(max_length=100, blank=True, null=True)

    def photo_preview(self):
        if self.photo:
            html = u'<a href="{0}" target="_blank"><img src="{1}"/></a>'
            return mark_safe(html.format(self.photo.url, self.photo.url))

    photo_preview.short_description = ''
    photo_preview.allow_tags = True


