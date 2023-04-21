from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField

blog_image_directory_path = "uploads/"


class Topic(models.Model):
    title = models.CharField(max_length=255)


class Blog(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 1
        PUBLISHED = 2
        UPDATED = 3

    blogs = models.Manager()
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='blogs',
    )

    status = models.IntegerField(default=Status.DRAFT,
                                 choices=Status.choices)

    title = models.CharField(max_length=255)
    body = QuillField()
    image = models.ImageField(
        upload_to=blog_image_directory_path,
        null=True,
        blank=True,
    )

    views = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class BlogTag(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='tags',
    )
    tag = models.CharField(max_length=255)


class BlogTopic(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='topics',
    )
    topic = models.ForeignKey(
        to=Topic,
        on_delete=models.CASCADE,
        related_name='blogs',
    )


class News(models.Model):
    news = models.Manager()
    blog = models.OneToOneField(
        Blog,
        on_delete=models.CASCADE,
        related_name='news',
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created', '-blog__id']

    def __str__(self):
        return self.blog.title


class BlogComment(models.Model):
    comments = models.Manager()
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    blog = models.ForeignKey(
        to=Blog,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    reply = models.ForeignKey(
        to="self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies',
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_all_childs(self):
        childs = [self]
        for comment in childs:
            for reply in comment.replies.all():
                childs.append(reply)

        childs.pop(0)
        childs.sort(key=lambda comment: comment.created)
        return childs

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.body


class BlogLike(models.Model):
    likes = models.Manager()
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='blog_likes',
    )
    blog = models.ForeignKey(
        to=Blog,
        on_delete=models.CASCADE,
        related_name='likes',
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class BlogCommentLike(models.Model):
    likes = models.Manager()
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='comment_likes',
    )
    comment = models.ForeignKey(
        to=BlogComment,
        on_delete=models.CASCADE,
        related_name='likes',
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
