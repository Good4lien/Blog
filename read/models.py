from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.safestring import mark_safe


class Books(models.Model):
    class Meta():
        verbose_name='Book'
        verbose_name_plural='Books'

    image_load = models.ImageField(null=True, blank=True, upload_to='media/reading/images/', verbose_name='', max_length=256)
    image = ImageSpecField(source='image_load', processors=[ResizeToFill(200, 300)], format='JPEG', options={'quality': 100})
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    html = RichTextUploadingField(null=True, blank=True)
    hold = models.BooleanField('Hold', default=False)
    css = models.TextField('CSS', max_length=1000, default='.css-title{font-size: 24px;}')

    def image_preview(self):
        if self.image:
            html = u'<a href="{0}" target="_blank"><img src="{1}"/></a>'
            return mark_safe(html.format(self.image_load.url, self.image.url))

    image_preview.short_description = 'Image'
    image_preview.allow_tags = True