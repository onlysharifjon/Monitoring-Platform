# views.py
from rest_framework import viewsets
from .serializers import BlogSerializer
from .models import Blog


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.blogs.all()
    serializer_class = BlogSerializer


from django.shortcuts import render

# Create your views here.
