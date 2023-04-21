# serializers.py
from rest_framework import serializers
from .models import Blog
from django_quill.fields import FieldQuill


class BlogSerializer(serializers.ModelSerializer):


    class Meta:
        model = Blog
        fields = '__all__'
