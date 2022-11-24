from multiprocessing import context
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import TemplateView 
from django.contrib.auth.decorators import login_required
from .models import  Group, Post, User
from .forms import PostForm


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    } 
    return render(request, 'posts/index.html', context)

def group_posts(request, slug): 
    group = get_object_or_404(Group, slug=slug) 
    post_list = group.posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = { 
        'title': 'Здесь будет информация о группах проекта Yatube',
        'group': group, 
        'page_obj': page_obj, 
    } 
    return render(request, 'posts/group_list.html', context) 


def profile(request, username):
    author = get_object_or_404(User, username=username)
    user_posts = author.posts.all()
    post_count = user_posts.count()
    paginator = Paginator(user_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    title = f'Профаил пользователя {username}'
    context = {
        'title': title,
        'page_obj': page_obj,
        'post_count': post_count,
        'author': author, 
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    author_post = post.author
    post_count = Post.objects.filter(author=author_post).count()
    title = f'Пост {post.text[0:30]}'
    context = {
        'post': post,
        'post_count': post_count,
        'title': title,
        'author_post': author_post,
    }
    return render(request, 'posts/post_detail.html', context)

@login_required 
def post_create(request):
    is_edit = False
    form = PostForm(request.POST or None)
    context = {
        'form': form,
        'is_edit': is_edit,
    }
    if request.method == 'POST':
        #form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            return redirect('posts:profile', post.author)
    return render(request, 'posts/post_create.html', context) 

@login_required
def post_edit(request, post_id):
    is_edit = True
    form = PostForm(request.POST)
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return redirect('posts:post_detail', post.id)
    #if request.method == "POST":
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:post_detail', post.id)
    context = { 
        'form': form,
        'is_edit': is_edit,
        'post': post,
    }
    return render(request, 'posts/post_create.html', context)
 
    
    
    