# serializers.py
from rest_framework import serializers
from .models import Blog, Teachers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'
