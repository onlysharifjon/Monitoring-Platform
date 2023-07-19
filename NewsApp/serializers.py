# serializers.py
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from .models import Blog


class ResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 30


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
