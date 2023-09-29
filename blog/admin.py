from django.contrib import admin
from .models import Post, Comment, RSS, Tag, ContentCat

admin.site.register(Tag)
admin.site.register(ContentCat)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(RSS)

