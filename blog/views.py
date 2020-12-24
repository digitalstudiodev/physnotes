from django.shortcuts import render, get_object_or_404, redirect, render
from users.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django import forms
from django.core.paginator import Paginator

def about(request):
    return render(request, "blog/about.html")

def contact(request):
    return render(request, "blog/contact.html")

class AuthorListView(ListView):
    model = Post
    template_name = 'blog/tag_list.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        user = self.kwargs["pk"]
        author = User.objects.all().filter(pk=user)[0]
        author_name = str(author.first_name) + " " + str(author.last_name)
        list_objs = []
        for obj in Post.objects.all():
            if obj.author == author:
                list_objs.append(obj)

        context = {
            'posts': list_objs,
            'header': author_name,
        }
        return context

class TagListView(ListView):
    model = Post
    template_name = 'blog/tag_list.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        tag = self.kwargs["tag"]
        list_objs = []
        for obj in Post.objects.all():
            for t in obj.tag:
                if t == tag:
                    list_objs.append(obj)

        context = {
            'posts': list_objs,
            'header': tag,
        }
        return context

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        featured = []
        for obj in Post.objects.all():
            for t in obj.tag:
                if t == "Featured":
                    featured.append(obj)
        recent = []
        for obj in Post.objects.all():
            for t in obj.tag:
                if t == "Recent":
                    recent.append(obj)
        popular = []
        for obj in Post.objects.all():
            for t in obj.tag:
                if t == "Popular":
                    popular.append(obj)
        context = {
            'popular': popular,
            'posts': Post.objects.all(),
            'featured': featured,
            'recent': recent,
        } 
        return context

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'preview', 'read_time', 'content' ,'tag', 'featured_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post

    fields = ['title', 'preview', 'read_time', 'content', 'tag', 'featured_image']

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
