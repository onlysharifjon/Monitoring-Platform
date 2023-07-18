from rest_framework.generics import RetrieveAPIView, ListAPIView
from .serializers import BlogSerializer
from .models import Blog


class AllBlogsView(ListAPIView):
    queryset = Blog.blogs.all()
    serializer_class = BlogSerializer


class SingleBlogView(RetrieveAPIView):
    queryset = Blog.blogs.all()
    serializer_class = BlogSerializer
