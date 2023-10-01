from typing import Any
from django.shortcuts import render, get_object_or_404, redirect, render
from users.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Post, Comment
from .forms import CommentForm
from django import forms
from django.core.paginator import Paginator
from blog.models import ContentCat, Tag
from .forms import PostForm, TagForm


def home(request):
    return render(request, "blog/blog.html")

def about(request):
    return render(request, "blog/about.html")

def categories(request):
    # convert tuple to list of categories
    categories = ContentCat.objects.all()
    context = {
        'categories': categories
    }
    return render(request, "blog/cat.html", context)


def category(request, pk):
    posts = Post.objects.all()
    category = ContentCat.objects.filter(pk=pk).first()
    tags = Tag.objects.filter(category=category)
    posts = posts.filter(tag__in=tags)
    context = {
        'items': posts,
        'category': category.category_name,
        'tags': tags
    }
    return render(request, "blog/cats.html", context)

def tagView(request, pk):
    posts = Post.objects.all()
    tag = Tag.objects.filter(pk=pk).first()
    posts = posts.filter(tag=tag)
    context = {
        'items': posts,
        'tag': tag,
        'categories': tag.category.all()
    }
    return render(request, "blog/tags.html", context)

def contact(request):
    return render(request, "blog/contact.html")

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'], tag_objects = Comment.objects.filter(post=self.object), []
        for i in self.object.tag.all():
            try:
                tag_objects.append(Tag.objects.all().filter(pk=i.pk).first())
            except:
                pass
        context['tags'] = tag_objects
        return context

class PostCreateView(LoginRequiredMixin, FormView):
    template_name="blog/post_form.html"
    form_class=PostForm
    success_url="/users/profile/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.save()
        if self.request.POST:
            tags, tag_objs = self.request.POST['tag'], []
            for i in tags:
                try:
                    tag_objs.append(Tag.objects.all().filter(pk=i).first())
                except:
                    pass
            form.instance.tag.set(tag_objs)
            form.instance.save()
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
    
# Category Views
class CategoryListView(ListView):
    model = ContentCat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = ContentCat
    fields = ['category_name']

    def form_valid(self, form):
        categories = ContentCat.objects.all()
        matched = categories.filter(category_name=form.instance.category_name)
        if len(matched) == 0:
            return super().form_valid(form)
        else:
            messages.info(self.request, "Category Already Exists, Rename Category")
            return redirect('blog:catgeory_create')

class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ContentCat

    fields = ['category_name']

    def form_valid(self, form):
        categories = ContentCat.objects.all()
        matched = categories.filter(category_name=form.instance.category_name)
        if len(matched) == 0:
            return super().form_valid(form)
        else:
            return messages.info(self.request, "Category Already Exists, Rename Category")

    def test_func(self):
        category = self.get_object()
        if category:
            return True
        return False

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ContentCat
    success_url = '/users/profile/'

    def test_func(self):
        category = self.get_object()
        if category:
            return True
        return False


class TagCreateView(LoginRequiredMixin, FormView):
    template_name="blog/tag_form.html"
    form_class=TagForm
    success_url="/users/profile/"

    def form_valid(self, form):
        form.instance.save()
        if self.request.POST:
            categories, category_objs = self.request.POST['category'], []
            for category in categories:
                category_objs.append(ContentCat.objects.all().filter(pk=category).first())
            form.instance.category.set(category_objs)
            form.instance.save()
        return super().form_valid(form)

class TagUpdateView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name="blog/tag_form.html"
    form_class=TagForm
    success_url="/users/profile/"

    def form_valid(self, form):
        if self.request.POST:
            # get category keys
            print(self.request.POST)
            categories, category_objs = list(self.request.POST['category']), []
            # get post object  
            tag_obj = Tag.objects.all().filter(tag_name=self.request.POST['tag_name']).first()
            # use category keys to get list of category objects
            print(len(categories))
            for i in range(len(categories)):
                print(categories[i])
                category_objs.append(ContentCat.objects.get(pk=int(categories[i])))
            # set the tag categories to the new category list
            print(category_objs)
            tag_obj.category.clear()
            tag_obj.category.set(category_objs)
            # save the tag with new info
            tag_obj.save()
        return super().form_valid(form)
    
    def test_func(self):
        return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Tag.objects.all().filter(pk=self.kwargs['pk']).first().category.all()
        category_pks = []
        for category in categories:
            category_pks.append(category.pk)
        context['form'].fields['tag_name'].initial = str(Tag.objects.all().filter(pk=self.kwargs['pk']).first().tag_name)
        context['form'].fields['category'].initial = category_pks
        return context

class TagDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tag
    success_url = '/users/profile/'

    def test_func(self):
        category = self.get_object()
        if category:
            return True
        return False