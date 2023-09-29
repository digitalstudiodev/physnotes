from django.urls import path, include
from .views import (home, PostDetailView, 
                    PostCreateView, PostUpdateView, 
                    PostDeleteView, about, 
                    contact, categories,
                    category,CommentCreateView)

app_name = 'blog'

urlpatterns = [
    path('about/', about, name='about'),
    path('categories/', categories, name='categories'),
    path('category/<id:category_id>/', category, name='category'),
    path('contact/', contact, name='contact'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', home, name='home'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    #
    path('post/<int:pk>/add_comment', CommentCreateView.as_view(), name="add_comment")
]