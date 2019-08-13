from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.safestring import mark_safe


class Tags(models.Model):
    class Meta():
        verbose_name='Tag'
        verbose_name_plural='Tags'

    title = models.CharField("Tag", max_length=50)

    def __str__(self):
        return self.title


class Posts(models.Model):
    class Meta():
        verbose_name='Post'
        verbose_name_plural='Posts'

    CATEGORIES = (
        ('none','None'),
        ('books','Book'),
        ('movies', 'Movie'),
        ('games', 'Game'),
    )
    category = models.CharField(max_length=100, choices=CATEGORIES, default='none', verbose_name='Category')
    image_load = models.ImageField(null=True, blank=True, upload_to = 'media/blog/images/', verbose_name='', max_length=256)
    image = ImageSpecField(source='image_load', processors=[ResizeToFill(300, 300)], format='JPEG', options={'quality': 100})
    title = models.CharField(max_length=100)
    preview = models.TextField(max_length=500)
    content = RichTextUploadingField(max_length=10000)
    tags = models.ManyToManyField(Tags, "Tags", blank=True)
    date = models.DateField(max_length=100, blank=True, null=True)
    likes = models.IntegerField(default=0, verbose_name='Likes')
    ip = models.TextField(blank=True, null=True, editable=False, default='0.0.0.0-')
    edit = models.TextField('',max_length=50, default='edit', editable=False)
    moderation = models.BooleanField('Moderation', default=False)
    hold = models.BooleanField('Hold', default=False)

    def __str__(self):
        return self.title

    def image_preview(self):
        if self.image:
            html=u'<a href="{0}" target="_blank"><img src="{1}"/></a>'
            return mark_safe(html.format(self.image_load.url, self.image.url))

    image_preview.short_description = 'Image'
    image_preview.allow_tags = True


class Messages(models.Model):
    class Meta():
        verbose_name='Message'
        verbose_name_plural='Messages'

    first_name = models.CharField('First_name', max_length=30)
    last_name = models.CharField('Last_name', max_length=30)
    email = models.EmailField('Email', max_length=30)
    subject =  models.CharField('Subject', max_length=50)
    message = models.TextField('message', max_length=500)

    def __str__(self):
        return self.subject


class Follow(models.Model):
    class Meta():
        verbose_name='Follower'
        verbose_name_plural='Followers'

    email = models.EmailField('Emal', max_length=100)

    def __str__(self):
        return self.email
