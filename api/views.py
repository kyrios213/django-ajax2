from django.shortcuts import render
from django.http import JsonResponse

from .models import Post
from .forms import PostForm
from profiles.models import Profile


def post_list_and_create(request):
    form = PostForm(request.POST or None)
    if request.is_ajax():
        if form.is_valid():
            author = Profile.objects.get(user=request.user)
            instance = form.save(commit=False)
            instance.author = author
            instance.save()
            return JsonResponse({
                'title': instance.title,
                'body': instance.body,
                'author': instance.author.user.username,
                'id': instance.id
            })
    context = {
        'form': form,
    }
    return render(request, 'posts/main.html', context)

def load_post_data_view(request, num_posts):
    if request.is_ajax():
        visible = 3
        upper = num_posts
        lower = upper - visible
        size = Post.objects.all().count()

        posts = Post.objects.all().order_by('-created')
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

def post_detail_data_view(request, pk):
    post = Post.objects.get(pk=pk)
    data = {
        'id': post.id,
        'title': post.title,
        'body': post.body,
        'author': post.author.user.username,
        'logged_in': request.user.username,
    }
    return JsonResponse({'data': data,})

def like_unlike_post(request):
    if request.is_ajax():
        pk = request.POST.get('pk')
        obj = Post.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)
        return JsonResponse({'liked': liked, 'count': obj.like_count})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostForm()

    context = {
        'post': post,
        'form': form,
    }

    return render(request, 'posts/detail.html', context)

def hello_world_view(request):
    return JsonResponse({'text': 'hello world'})