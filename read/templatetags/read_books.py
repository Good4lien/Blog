from django import template
from read.models import Books


register = template.Library()

@register.inclusion_tag('read/read.html')

def show_books():
  books = Books.objects.all()
  return {'books': books}