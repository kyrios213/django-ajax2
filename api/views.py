from django.shortcuts import render
from django.http import JsonResponse

from .models import Post


def post_list_and_create(request):
    posts = Post.objects.all()
    return render(request, 'posts/main.html', {'posts': posts})

def load_post_data_view(request, num_posts):
    visible = 3
    upper = num_posts
    lower = upper - visible
    size = Post.objects.all().count()

    posts = Post.objects.all().order_by('id')
    data = []
    for post in posts:
        item = {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'liked': True if request.user in post.liked.all() else False,
            'count': post.like_count,
            'author': post.author.user.username,
        }
        data.append(item)
    return JsonResponse({'data': data[lower:upper], 'size': size})

def hello_world_view(request):
    return JsonResponse({'text': 'hello world'})