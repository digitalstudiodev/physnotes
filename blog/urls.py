from django.urls import path, include
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, TagListView, AuthorListView, about, contact)

app_name = 'blog'

urlpatterns = [
    path('tag/<str:tag>/', TagListView.as_view(), name='tag'),
    path('author/<int:pk>/', AuthorListView.as_view(), name='author'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]