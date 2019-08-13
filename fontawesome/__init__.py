from django.conf import settings
from django.utils.html import format_html

class Icon(object):

    def __init__(self, id):
        self.id = id

    def as_html(self):
        if not self.id:
            return ''

        prefix = getattr(settings, 'FONTAWESOME_PREFIX', 'fa')
        return format_html('<i class="{0} {0}-{1}"></i>', prefix, self.id)

    def __str__(self):
        return self.id

    def __unicode__(self):
        return str(self)