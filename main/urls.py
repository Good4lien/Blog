from django.urls import path
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView, UpdateView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.core.paginator import Paginator
from .models import Posts
from . import views


urlpatterns = [
    path('recs', views.recs, name='recs'),
    path('contact', views.cont, name='cont'),
    path('srch', views.search, name='search'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^posts/addlike/(?P<post_id>\d+)/$', views.add_like),
    url(r'^post/(?P<pk>\d+)$', DetailView.as_view(model = Posts, template_name="blog/post.html")),
    path('mod', ListView.as_view(queryset=Posts.objects.all().order_by("-date").order_by("title").filter(moderation=False), paginate_by=5, template_name='blog/mod.html'), name='mod'),
    path('new', ListView.as_view(queryset=Posts.objects.all().order_by("-date").order_by("title").filter(moderation=True), paginate_by=5, template_name='blog/blog.html'), name='new'),
    path('', ListView.as_view(queryset=Posts.objects.all().order_by("-date").order_by("title").filter(moderation=True, hold=True), paginate_by=5, template_name='blog/blog.html'), name='blog'),
    path('books', ListView.as_view(queryset=Posts.objects.all().order_by("-date").order_by("title").filter(category='books', moderation=True), paginate_by=5, template_name='blog/blog.html'), name='books'),
    path('games', ListView.as_view(queryset=Posts.objects.all().order_by("-date").order_by("title").filter(category='games', moderation=True), paginate_by=5, template_name='blog/blog.html'), name='games'),
    path('movies', ListView.as_view(queryset=Posts.objects.all().order_by("-date").order_by("title").filter(category='movies', moderation=True), paginate_by=5, template_name='blog/blog.html'), name='movies'),
]


if settings.DEBUG:
    urlpatterns+=staticfiles_urlpatterns()+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)