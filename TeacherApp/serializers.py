from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from .models import Teacher, Lesson


class ResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


class TeacherSerializer(serializers.ModelSerializer):
    scientific_title = serializers.SlugField('title')
    scientific_degree = serializers.SlugField('title')
    education_level = serializers.SlugField('title')
    specialty = serializers.SlugField('title')
    foreign_langs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Teacher
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    room = serializers.SlugField("title")
    teacher = serializers.SlugField("full_name")
    subject = serializers.SlugField("full_name")
    group = serializers.SlugField("full_name")

    class Meta:
        model = Lesson
        fields = "__all__"
