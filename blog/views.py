from django.shortcuts import render, get_object_or_404, redirect, render
from users.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm
from django import forms
from django.core.paginator import Paginator
from .dict_lib import TAG_OPTIONS

def home(request):
    return render(request, "blog/blog.html")

def about(request):
    return render(request, "blog/about.html")

def categories(request):
    # convert tuple to list of categories
    cat = []
    for i in TAG_OPTIONS:
        cat.append(i[0])
    context = {
        'categories': cat
    }
    return render(request, "blog/cat.html", context)


def category(request, category):
    list_objs = []
    for obj in Post.objects.all():
        for tagg in list(obj.tag):
            if tagg == category:
                list_objs.append(obj)
    context = {
        'items': list_objs,
        'category': category
    }
    return render(request, "blog/cats.html", context)

def contact(request):
    return render(request, "blog/contact.html")

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'preview', 'read_time', 'content' ,'tag', 'featured_image','note']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post

    fields = ['title', 'preview', 'read_time', 'content', 'tag', 'featured_image','note']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CommentCreateView(CreateView):
    model = Comment
    fields = ['user', 'comment']

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_id'] = self.kwargs["pk"]
        return context

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post:
            return True
        return False