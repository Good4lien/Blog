from django.http.response import  HttpResponse, Http404
from django.shortcuts import render_to_response, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic import View
from .models import Posts
from .forms import FollowForm, MessageForm


def user_ip(request):
    ip = request.META.get('REMOTE_ADDR', '/')
    return ip


def return_path(request):
    path = request.META.get('HTTP_REFERER', '/')
    return path


def search_query(request):
    query = request.GET.get('search', '')
    return query


def recs(request):
    path = 'blog/recs.html'
    return render(request, path)


def cont(request):
    path = 'blog/cont.html'
    if request.method == 'POST':
        follow_form = FollowForm(request.POST, prefix='follow')
        mess_form = MessageForm(request.POST, prefix='message')
        if follow_form.is_valid():
            follow_form.save()
        if mess_form.is_valid():
            mess_form.save()
    else:
        follow_form = FollowForm(prefix='follow')
        mess_form = MessageForm(prefix='message')
    return render(request, path, context={'follow_form' : follow_form, 'mess_form' : mess_form})


def add_like(request, post_id):
    try:
        post = Posts.objects.get(id=post_id)
        if not(user_ip(request) in post.ip):
            post.ip+=user_ip(request).__str__()
            post.ip+='-'
            post.likes +=1
            post.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect(return_path(request))


def search(request):
    query = search_query(request)
    if query:
        result = Posts.objects.all().order_by("title").filter(moderation=True).filter(
            Q(title__icontains=query) |
            Q(preview__icontains=query) |
            Q(tags__title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__icontains=query) |
            Q(date__icontains=query)
        ).distinct('title')
        if result:
            return ListView.as_view(queryset=result, paginate_by=5, template_name='blog/blog.html')(request)
        else:
            return redirect(return_path(request))
    else:
        return redirect(return_path(request))



