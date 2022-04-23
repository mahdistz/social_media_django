from django.http import HttpResponse
from .models import User, Post, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import NewPostForm, NewCommentForm
from django.contrib import messages


class NewPost(View):

    def post(self, request):
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'mysite/new_post.html', {'form': form, 'img_obj': img_obj})

    def get(self, request):
        form = NewPostForm()
        return render(request, 'mysite/new_post.html', {'form': form})


class PostList(ListView):
    model = Post


class PostDetail(View):
    template = 'mysite/post_detail.html'
    form_class = NewCommentForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, pk=kwargs['post_id'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        comments = post.post_comment.all()
        return render(request, self.template, {'post': post, 'comments': comments, 'forms': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = self.post_instance
            new_comment.save()
            return redirect('post_detail', new_comment.post.id)


class PostRecently(View):
    template = 'mysite/recently.html'

    def get(self, request):
        posts = Post.objects.get_query_set().all()
        return render(request, self.template, {'posts': posts})


def all_posts(request):
    posts = Post.objects.all().values()
    return HttpResponse(posts)


def all_users(request):
    users = User.objects.all().values()
    return HttpResponse(users)


def posts_of_user(request, id):
    posts = Post.objects.filter(user_id=id).values()
    return HttpResponse(posts)


def post_information(request, id):
    info = Post.objects.filter(post_id=id).values()
    return HttpResponse(info)


def user_info(request, id):
    detail = User.objects.filter(id=id).values()
    return HttpResponse(detail)


def comments(request, id):
    comment = Comment.objects.filter(id=id).values()
    return HttpResponse(comment)


def index(request):
    return render(request, 'mysite/index.html', {})
