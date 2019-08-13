from django import template
from instagram.models import Posts
from blog.settings import INSTAGRAM_URL



register = template.Library()

@register.inclusion_tag('instagram/instagram.html')
def instagram():
  posts = Posts.objects.all().order_by("-date")[:8]
  return {'posts': posts, 'INSTAGRAM_URL':INSTAGRAM_URL}

@register.inclusion_tag('instagram/widget.html')
def instagram_widget():
  posts = Posts.objects.all().order_by("-date")[:6]
  return {'posts': posts, 'INSTAGRAM_URL':INSTAGRAM_URL}