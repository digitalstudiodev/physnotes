from django.urls import path, include
from .views import (home, PostDetailView, 
                    PostCreateView, PostUpdateView, 
                    PostDeleteView, about, 
                    contact, categories,
                    category,CommentCreateView,tagView,
                    CategoryCreateView,CategoryUpdateView,CategoryDeleteView, CategoryListView, TagUpdateView, TagDeleteView, TagCreateView)

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('categories/', categories, name='categories'),
    path('category/<int:pk>/', category, name='category'),
    path('category/tag/<int:pk>/', tagView, name='tag'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/add_comment', CommentCreateView.as_view(), name="add_comment"),
    path('category/new/', CategoryCreateView.as_view(), name='category_create'),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/update', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete', CategoryDeleteView.as_view(), name='category_delete'),
    path('tag/create/', TagCreateView.as_view(), name='tag_create'),
    path('tag/<int:pk>/update', TagUpdateView.as_view(), name='tag_update'),
    path('tag/<int:pk>/delete', TagDeleteView.as_view(), name='tag_delete'),
]