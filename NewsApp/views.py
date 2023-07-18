from requests import Response
from rest_framework import viewsets
from .serializers import BlogSerializer, TeacherSerializer
from .models import Blog, Teachers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView


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


class TeacherInfoView(APIView):
    @swagger_auto_schema(request_body=TeacherSerializer)
    def get(self, request):
        # blog objects send all
        blogs = Teachers.objects.all()
        serializer = TeacherSerializer(blogs, many=True)
        return Response(serializer.data)


from django.shortcuts import render

# Create your views here.
