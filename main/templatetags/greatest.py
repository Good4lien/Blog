from django import template
from main.models import Posts


register = template.Library()

@register.inclusion_tag('blog/includes/greatests_posts.html')

def show_greatest():
  q = Posts.objects.all().filter(moderation=True).order_by("-likes")[:3]
  return {'q': q}