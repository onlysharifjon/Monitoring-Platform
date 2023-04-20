from django.contrib import admin

from .models import Topic, Blog, BlogTag, BlogTopic, News, BlogComment, BlogLike, BlogCommentLike

admin.site.register([Topic, Blog, BlogTag, BlogTopic, News, BlogComment, BlogLike, BlogCommentLike])
