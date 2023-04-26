from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

blog_image_directory_path = "uploads/"


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
    body = RichTextUploadingField()
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

    def get_all_children(self):
        children = [self]
        for comment in children:
            for reply in comment.replies.all():
                children.append(reply)

        children.pop(0)
        children.sort(key=lambda x: x.created)
        return children

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
