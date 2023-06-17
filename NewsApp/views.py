from requests import Response
from rest_framework import viewsets
from .serializers import BlogSerializer
from .models import Blog
from drf_yasg.utils import swagger_auto_schema


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.blogs.all()
    serializer_class = BlogSerializer

    @swagger_auto_schema(request_body=BlogSerializer)
    def get(self, request):
        # blog objects send all
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



from django.shortcuts import render

# Create your views here.
