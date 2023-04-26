from django.contrib import admin

from .models import Blog, BlogTag, BlogComment, BlogLike, BlogCommentLike

admin.site.register([Blog, BlogTag, BlogComment, BlogLike, BlogCommentLike])
