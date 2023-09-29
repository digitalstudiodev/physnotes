from django.db import models
from django.utils import timezone
from users.models import User
from django.urls import reverse
from multiselectfield import MultiSelectField
from PIL import Image
from .dict_lib import TAG_OPTIONS

# Data Category - i.e. Physics, Math, Chemistry
class ContentCat(models.Model):
    category_name = models.CharField(max_length=100, default=None)
    
    def __str__(self):
        return self.category_name

# Content Tag - i.e. Nuclear, Optics, Environmental
class Tag(models.Model):
    tag_name = models.CharField(max_length=100, default=None)
    category = models.ForeignKey(ContentCat, on_delete=models.CASCADE, default=None, null=True)
    
    def __str__(self):
        return self.tag_name

# Curated Content - Free
class Post(models.Model):
    title = models.CharField(max_length=100, default=None)
    preview = models.CharField(max_length=5000, default=None)
    content = models.TextField(default=None, verbose_name="Content")
    date_posted = models.DateTimeField(default=timezone.now)
    read_time = models.IntegerField(default=5, verbose_name="Read Time", help_text="in minutes")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, default=None, null=True)
    featured_image = models.ImageField(default='default.png', upload_to='blog_pics', verbose_name="Featured Image")
    note = models.FileField(default=None, upload_to='notes', verbose_name="Notes", null=True, blank=True, help_text="(Optional)")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

# User Comment on Curated Content
class Comment(models.Model):
    user = models.CharField(max_length=100, default=None, verbose_name="Name")
    comment = models.TextField(default=None, verbose_name="Comment")
    date_posted = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.post.pk})
    
# Data from RSS Feeds    
class RSS(models.Model):
    title = models.CharField(max_length=100, default=None)
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING, default=None, null=True)
    summary = models.CharField(max_length=5000, default=None)
    content = models.TextField(default=None, verbose_name="Content")
    story_link = models.CharField(max_length=5000, default=None)
    media_link = models.CharField(max_length=5000, default=None)
    date_posted = models.DateTimeField(default=None)

    def __str__(self):
        return self.title